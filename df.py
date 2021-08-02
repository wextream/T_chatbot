import pandas as pd
import numpy as np
import math

file_name = 'ExportLTE2125.csv'

def get_distance(data,lat,long):
    earth_radius=6371
    lat1 = data["Latitude"]
    lon1 = data["Longtitude"]
    lat2 = lat
    lon2 = long
    lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])
    a = np.sin((lat2-lat1)/2.0)**2 +  np.cos(lat1) * np.cos(lat2) * np.sin((lon2-lon1)/2.0)**2
    distance = (earth_radius * 2 * np.arcsin(np.sqrt(a)))
    return (distance)

def Get_angle(data,lat,long):
    lat1 = data["Latitude"]
    lon1 = data["Longtitude"]
    D = data['Distances(Km)']
    delta_lat = math.sqrt((lat1-lat)**2)
    d = 110.574*(delta_lat)
    if lat1 > float(lat) and lon1 < float(long) :
        angle = math.acos(d/D)
        angle_in_degree = angle*180/math.pi
        angle_by_normal = angle_in_degree + 270
    if lat1 < float(lat) and lon1 < float(long) :
        angle = math.asin(d/D)
        angle_in_degree = angle*180/math.pi
        angle_by_normal = angle_in_degree
    if lat1 > float(lat) and lon1 > float(long) :
        angle = math.acos(d/D)
        angle_in_degree = angle*180/math.pi
        angle_by_normal = 270 - angle_in_degree
    if lat1 < float(lat) and lon1 > float(long) :
        angle = math.acos(d/D)
        angle_in_degree = angle*180/math.pi
        angle_by_normal = 90 + angle_in_degree
    return angle_by_normal


def convert_Azimuth(data):
    Azimuth = data['Logical Azimuth']
    if Azimuth >= 0.0 and Azimuth <= 90.0:
        o = 90 - Azimuth
    else:
        o = 450 - Azimuth
    return o


def Coverage_range(data):
    Ref_Az  = data['Ref Azimuth']
    BW = data['Beamwidth']
    BW_d = BW/2
    UB = Ref_Az + BW_d
    LB = Ref_Az - BW_d
    return [LB,UB]


def enodeBIDseach(input,file_name):
    df = pd.read_csv(file_name)
    df_1 = df[['eNodeB ID']].astype(str)
    df_enode = df[df_1['eNodeB ID']==input]
    df_enode_siteID = df_enode[['eNodeB ID','Site ID']]
    df_enode_siteID = df_enode_siteID.drop_duplicates(['eNodeB ID','Site ID'])
    df_out = df_enode_siteID['Site ID']
    site_ID = df_out.to_list()[0]
    return site_ID

def Get_nearest_site(Latitude,Longitude,file_name):
    lat1 = float(Latitude)
    long1 = float(Longitude)
    df = pd.read_csv(file_name)
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longtitude'] = df['Longtitude'].astype(float)
    df_1 = df[['Site ID','Latitude','Longtitude']]
    df_1['Distances(Km)'] = df_1.apply(get_distance,axis=1,lat=lat1,long=long1)
    df_1 = df_1.drop_duplicates(['Site ID','Distances(Km)'])
    df_distance = df_1.sort_values(by=['Distances(Km)'])
    out = df_distance.head(10)[['Site ID','Distances(Km)']].to_string(index=False)
    return out

def Distance_Angle_f_site(Latitude,Longitude,input,file_name):
    df = Get_Angle_f_site(Latitude,Longitude,file_name)[3]
    df_1 = df[df['Site ID']==input]
    out_str = df_1[['Site ID','Vector Angle','Distances(Km)']].to_string(index=False)
    return out_str


def Get_Angle_f_site(Latitude,Longitude,file_name):
    lat1 = float(Latitude)
    long1 = float(Longitude)
    df = pd.read_csv(file_name)
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longtitude'] = df['Longtitude'].astype(float)
    df_1 = df[['Site ID','Latitude','Longtitude']]
    df_1['Distances(Km)'] = df_1.apply(get_distance,axis=1,lat=lat1,long=long1)
    df_distance = df_1.sort_values(by=['Distances(Km)'])
    df_distance['Vector Angle'] = df_distance.apply(Get_angle,axis=1,lat=lat1,long=long1)
    df_vector = df_distance.drop_duplicates(['Site ID','Vector Angle'])
    df_out = df_vector.head(10)
    out_str = df_out[['Site ID','Vector Angle']].to_string(index=False)
    site_list = list(df_out['Site ID'].unique())
    df_ref = df_out[['Site ID','Vector Angle']]
    return [out_str,site_list,df_ref,df_vector]

def Compare_angle(Latitude,Longitude,file_name,System):
    df = pd.read_csv(file_name)
    df_lo = df[['Logical Azimuth','Site ID','Cell Name','System']]
    df_lo['Logical Azimuth'] = df_lo['Logical Azimuth'].astype(float)
    df_lo['Ref Azimuth'] = df_lo.apply(convert_Azimuth,axis=1)
    Ref_object = Get_Angle_f_site(Latitude,Longitude,file_name)
    b = Ref_object[2].head(5)
    l_out = []
    Cell_name_out =[]
    delta_angle_list = []
    for index , rows in b.iterrows():
        S = rows['Site ID']
        V = rows['Vector Angle']
        #print(S,V)
        df_lo_test = df_lo[df_lo['Site ID']==S]
        for index , lows in df_lo_test.iterrows():
            Site_ref = [lows['Site ID'],lows['Cell Name'],lows['System'],lows['Ref Azimuth']]
            #print(Site_ref)
            delta_angle = V - Site_ref[3]
            delta_angle_list.append(delta_angle)
            if delta_angle <= 60 and delta_angle >= -60 :
                if Site_ref[2]==System:
                    Cell_name_out.append([Site_ref[0],Site_ref[1],Site_ref[2]])
                    l_out.append([Site_ref[1],Site_ref[2]])
    df_l_out = pd.DataFrame(columns=['Cell Name','System'],data=l_out)
    Last_out = df_l_out.to_string(index=False)
    return Last_out
    
def Cell_in_target(Latitude,Longitude,input,file_name1,file_name2):
    lat1 = float(Latitude)
    long1 = float(Longitude)
    df = pd.read_csv(file_name1)
    df1 = pd.read_csv(file_name2)
    df1_i = df1[['Site ID','Cell Name','Beamwidth','Logical Azimuth']]
    df1_i['Ref Azimuth'] = df1_i.apply(convert_Azimuth,axis=1)
    df1_i['Cover range'] = df1_i.apply(Coverage_range,axis=1)
    df1_i = df1_i[df1_i['Site ID']==input]
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longtitude'] = df['Longtitude'].astype(float)
    df_1 = df[['Site ID','Latitude','Longtitude']]
    df_target = df_1[df_1['Site ID']==input]
    df_target['Distances(Km)'] = df_target.apply(get_distance,axis=1,lat=lat1,long=long1)
    df_target['Vector Angle'] = df_target.apply(Get_angle,axis=1,lat=lat1,long=long1)
    df_target = df_target.drop_duplicates(['Site ID','Vector Angle'])
    ang_out = list(df_target['Vector Angle'].unique())[0]
    l_out = []
    for index , rows in df1_i.iterrows():
        UB = rows['Cover range'][1]
        LB = rows['Cover range'][0]
        Cell_name = rows['Cell Name']
        if UB>0 and LB>0:
            c1 = UB - ang_out
            c2 = ang_out - LB
            if c1>0 and c2>0:
                l_out.append(Cell_name)
        else:
            c3 = UB - ang_out
            if c3>0:
                l_out.append(Cell_name)
            else:
                A_ref = ang_out - 360
                c4 = A_ref - LB
                if c4>0:
                    l_out.append(Cell_name) 
    df_out = pd.DataFrame(columns=['Cell Name'],data=l_out).to_string(index=False)
    if l_out == [] :
        df_out = 'ไม่มีCellที่ยิงมาหาคุณ' 
    return df_out
