import experiment_manager as xp_man
import naminggamesal as ngal

from experiment_manager.metaexp.metaexp import MetaExperiment


#### Function to construct the coinfiguration of each simulation, depending on a few parameters, described below ####

def xp_cfg(N,M,W,time_scale,active,gamma):
    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": 'matrix_new'
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": "minimal"
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": N, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": M, #number of meanings
              "W": W  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            }
          }
        }
    if active:
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'strat_type':'lapsmax_mab_explothreshold','bandit_type':'bandit_laps','gamma':gamma,'time_scale':time_scale,
                "memory_policies": [{
                      "time_scale": time_scale,
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    return base_cfg


#### Function to determine the number of time steps for each simulation ####

def Tmax_func(N,M,W,time_scale,active,gamma):
  return 100000


#### Number of trials per distinct configuration ####

nbiter = 8


#### Description of the parameters of experiment configuration ####

params = {'N':{'default_value':40,'label':'population size','values':[40],'min':0},
          'M':{'default_value':40,'label':'#meanings','values':[40],'min':0},
          'W':{'default_value':40,'label':'#words','values':[40],'min':0},
          'time_scale':{'default_value':1,'label':'time scale','values':[1,2,3,4,5,6,7,8,9,10,20,30,50],'min':0,'max':30,'short_label':'$\\tau$','unit_label':'Time scale $\\tau$'},
          'gamma':{'default_value':0.01,'values':[0.01,1.],'min':0,'max':1.,'short_label':'$\\gamma$','label':'exploration coefficient'},
          'active':{'default_value':False,'values':[False,True]}
        }



#### Measures, to be found in naminggamesal.ngmeth ####

local_measures = {'srtheo':{'label':'Theoretical Communicative Success'},
            'Nlink':{'unit_label':'#associations','label':'Local Complexity'},
            'N_d':{'unit_label':'#associations','label':'Global Complexity'}}
global_measures = {'conv_time':{'unit_label':'#interactions','label':'Convergence Time'},
                    'max_mem':{'unit_label':'#associations','label':'Maximum Local Complexity'},
                    'max_N_d':{'unit_label':'#associations','label':'Maximum Global Complexity'},
                    }


#### Defining the MetaExperiment object, containing all this information ####

meta_exp = MetaExperiment(params=params,
              local_measures=local_measures,
              global_measures=global_measures,
              xp_cfg=xp_cfg,
              Tmax_func=Tmax_func,
              default_nbiter=nbiter,
              time_label='#interactions',
              time_short_label='T',
              time_max=80000,
              time_min=0)

#### Parameters for running the simulations. By default, using all available cores on local computer ####


jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}
jq_cfg_plafrim = {'jq_type':'plafrim','erase':True,
         'modules':['language/python/3.5.2'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+https://github.com/wschuell/experiment_manager.git@origin/develop#egg=experiment_manager',
    '-e git+https://github.com/flowersteam/naminggamesal.git@origin/develop#egg=naminggamesal'
]}
jq_cfg_avakas = {'jq_type':'avakas','erase':True,
         'modules':['python3/3.6.0'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+ssh://git@github.com/wschuell/experiment_manager.git@develop#egg=experiment_manager',
    '-e git+ssh://git@github.com/flowersteam/naminggamesal.git@develop#egg=naminggamesal'
]}



db = ngal.ngdb.NamingGamesDB(do_not_close=True)
meta_exp.set_db(db)

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)
#meta_exp.set_batch(jq_cfg=jq_cfg_plafrim,estimated_time=1200)
#meta_exp.set_batch(jq_cfg=jq_cfg_avakas,estimated_time=1200)

meta_exp.default_batch='local_multiprocess'
