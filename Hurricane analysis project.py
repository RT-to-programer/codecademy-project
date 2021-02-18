# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damage(damages):
    for i in range(len(damages)):
        if 'M' in damages[i]:
            milion = float(damages[i].replace('M','')) * 1000000
            damages[i] = milion

        elif 'B' in damages[i]:
            bilion = float(damages[i].replace('B','')) * 1000000000
            damages[i] = bilion

    return damages        

# write your construct hurricane dictionary function here:
def dic_by_name(hurricane):
    all_data = zip(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
    new = {'Name':None, 'Year':None, 'Month':None, 'Max_sustained_winds':None, 'Areas_affected':None, 'Damage':None, 'Death':None}
    for i in all_data:
        if hurricane in i:
            new['Name'],new['Year'],new['Month'],new['Max_sustained_winds'],new['Areas_affected'],new['Damage'],new['Death'] = i

    return new

def list_of_hurricane_dic():
    all_data = zip(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
    dic = []
    for i in all_data:
        new = {'Name':None, 'Year':None, 'Month':None, 'Max_sustained_winds':None, 'Areas_affected':None, 'Damage':None, 'Death':None}
        new['Name'],new['Year'],new['Month'],new['Max_sustained_winds'],new['Areas_affected'],new['Damage'],new['Death'] = i
        dic.append(new)

    return dic

# write your construct hurricane by year dictionary function here:
def dic_by_year(year):
    all_data = zip(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
    lst = []
    for i in all_data:
        new = {'Name':None, 'Year':None, 'Month':None, 'Max_sustained_winds':None, 'Areas_affected':None, 'Damage':None, 'Death':None}
        if year in i:
            new['Name'],new['Year'],new['Month'],new['Max_sustained_winds'],new['Areas_affected'],new['Damage'],new['Death'] = i
            lst.append(new)
    return lst

# write your count affected areas function here:
def dic_by_area_frequency(area= areas_affected):
    dic = {}
    for i in area:
        for area in i:
            if area not in dic:
                dic[area] = 1
            if area in dic:
                dic[area] += 1

    return dic

# write your find most affected area function here:
def most_affected_area(dic):
    return max(dic, key= dic.get)


# write your greatest number of deaths function here:
def most_death(dic=list_of_hurricane_dic()):
    result = {}
    for hurricane in dic:
        result[hurricane['Name']] = hurricane['Death']
    
    name, death = max(result, key=result.get), result[max(result, key=result.get)]
    
    return name,death

# write your catgeorize by mortality function here:
def mortality_rating():
    hurricane_mortality = list(zip(names, deaths))
    mortality_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane, mortality in hurricane_mortality:
        if mortality <= 0:
            mortality_scale[0].append(hurricane)
        elif mortality <= 100:
            mortality_scale[1].append(hurricane)
        elif 100 < mortality <=500:
            mortality_scale[2].append(hurricane)
        elif 500 < mortality <= 1000:
            mortality_scale[3].append(hurricane)
        elif 1000 < mortality <= 10000:
            mortality_scale[4].append(hurricane)
        else:
            mortality_scale[5].append(hurricane)
    
    return mortality_scale

# write your greatest damage function here:
def greatest_damage():    
    hurricane_damage = list(zip(names, damages))
    for i in hurricane_damage:
        if type(i[1]) == str:
            hurricane_damage.remove(i)

    return max(hurricane_damage, key= lambda x: x[1])

# write your catgeorize by damage function here:
def damage_rating():
    hurricane_damage = list(zip(names, damages))
    damage_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane, damage in hurricane_damage:
        if type(damage) == str :
            damage_scale[0].append(hurricane)
        elif 0 < damage <= 100000000:
            damage_scale[1].append(hurricane)
        elif 100000000 < damage <= 1000000000:
            damage_scale[2].append(hurricane)
        elif 1000000000 < damage <= 10000000000:
            damage_scale[3].append(hurricane)
        elif 10000000000 < damage <= 50000000000:
            damage_scale[4].append(hurricane)
        else:
            damage_scale[5].append(hurricane)
    
    return damage_scale
