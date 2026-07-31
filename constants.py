# # Name of all PFTs
# PFT = [ 'TChla','Diatoms','Dinoflagelllates', 'Haptophytes','Chlorophytes','Prochl','Cyano_noProchl']

# # PFT concentration reliable range
# PFT_limits ={'TChla':          (0.001,50),
#             'Diatoms':         (0.001,50),
#             'Dinoflagelllates':(0.001,50),
#             'Haptophytes':     (0.001,10),
#             'Prochl':          (0.001, 5),
#             'Proka':           (0.001, 5),
#             'Chlorophytes':    (0.001,10)}


# PFT_longname= {
#     'TChla':'Total Chlorophyll a',
#     'Haptophytes':'Haptophytes',
#     'Diatoms':'Diatoms',
#     'Dinoflagelllates':'Dinoflagelllates',
#     'Proka':'Prokaryotic Phytop.',
#     'cyano_noProchlo':r'Cyanobacteria W/O $\mathit{Prochlorococcus}$',
#     'Chlorophytes':'Chlorophytes',
#     'cryptophytes':'Cryptophytes',
#     'chrysophytes':'Chrysophytes',
#     'Prochl':r'$\mathit{Prochlorococcus}$',
# }


# Name of all PFTs
PFT = ['CHL', 'DIATO', 'DINO', 'HAPTO', 'GREEN', 'PROKAR']

# PFT concentration reliable range
PFT_limits ={'CHL': (0.001,50),
            'DIATO':(0.001,50),
            'DINO':(0.001,50),
            'HAPTO':(0.001,10),
            'PROKAR':(0.001, 5),
            'GREEN':(0.001,10)}


PFT_longname= {
    'CHL':'Total Chlorophyll-a',
    'HAPTO':'Haptophytes',
    'DIATO':'Diatoms',
    'DINO':'Dinoflagelllates',
    'PROKAR':'Prokaryotic Phytop.',
    'GREEN':'Green algae',
}