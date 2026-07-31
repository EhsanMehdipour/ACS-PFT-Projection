import numpy as np

params = {
    'PFT': [
        'CHL',
        'DIATO',
        'DINO',
        'HAPTO',
        'GREEN',
        'PROKAR',
    ],

    'PFT_longname': {
        'CHL':'Total Chlorophyll a', 
        'DIATO':'Diatoms', 
        'DINO':'Dinoflagellates', 
        'HAPTO':'Haptophyte',
        'GREEN':'Green Algae', 
        # 'PROCHLO':r"$\it{Prochlorococcus}$",
        'PROKAR':'Prokaryotic P.',
    },
    
    'PFT_HPLC_dict': {
        'Diatoms': 'DIATO',
        'Dinoflagelllates': 'DINO',
        'Chlorophytes': 'GREEN',
        'Haptophytes': 'HAPTO',
        'Prochl': 'PROCHLO',
        'Cyano_noProchl': 'PROKAR',
        'TChla': 'CHL'
    },
    
    'PFT_ACS_dict': {
        'TChla':'CHL',
        'Haptophytes':'HAPTO',
        'Diatoms':'DIATO',
        'Dinoflagelllates':'DINO',
        'Proka':'PROKAR',
        'Chlorophytes':'GREEN',
        # 'Prochl':'PROCHLO'
    },
    
    'UNC' :[
        'CHL_uncertainty',
        'DIATO_uncertainty',
        'DINO_uncertainty',
        'HAPTO_uncertainty',
        'GREEN_uncertainty',
        'PROKAR_uncertainty',
    ],
    
    
    'UNC_dict': {
        'CHL_uncertainty':'CHL',
        'DIATO_uncertainty':'DIATO',
        'DINO_uncertainty':'DINO',
        'HAPTO_uncertainty':'HAPTO',
        'GREEN_uncertainty':'GREEN',
        'PROKAR_uncertainty':'PROKAR',
    },
    
    'DINCAE_error_dict':{
        'CHL_error':'CHL',
        'DIATO_error':'DIATO',
        'DINO_error':'DINO',
        'HAPTO_error':'HAPTO',
        'GREEN_error':'GREEN',
        'PROKAR_error':'PROKAR',
    },
    
    'plot_labels' : np.array([
        0.001,0.003,0.006,
        0.01,0.03,0.06,
        0.1,0.3,0.6,
        1,3,6,
        10,30,60,100,
    ]),
    
    'start_date' : np.datetime64('2016-04-25'),
    'end_date' : np.datetime64('2019-04-25'),
    'expedition_start_date': np.datetime64('2018-05-10'),
    'expedition_end_date' : np.datetime64('2018-06-09'),
    'delta': np.timedelta64(3, 'D'),
    'units': r'$\frac{mg}{m^{3}}$'
    
}

params['ALL_data'] = params['PFT'] + params['UNC'] + ['flags']

sst_rename = {'latitude':'lat','longitude':'lon','analysed_sst':'sst'}