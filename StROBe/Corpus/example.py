import os
import sys

strobeDir = os.path.dirname(os.path.realpath(__file__)) # get path where this file is (StROBe path)
sys.path.append(os.path.join(strobeDir, 'Corpus')) 

import Corpus.feeder as fee
import Corpus.residential as res

os.chdir(os.path.join(strobeDir, 'Corpus')) # make Corpus the current directory

# Create and simulate a single household, with given type of members, and given year
family = res.Household("Example household", members=['FTE', 'Unemployed'])
family.simulate(year=2013, ndays=365)

family.__dict__ # list all elements of family for inspection


# Simulate households for an entire feeder

cleanup = True #choose whether individual household results will be deleted or not
# create folder where simulations will be stored for feeder
dataDir = os.path.join(strobeDir,"Simulations")
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
    
# Test feeder with 5 households, temperatures given in Kelvin
fee.IDEAS_Feeder(name='Household',nBui=5, path=dataDir, sh_K=True)

# cleanup pickled household files from new folder (only keep text files with results)
if cleanup:
    for file in os.listdir(dataDir):
        print(file)
        if file.endswith(('.p')):
            os.remove(os.path.join(dataDir, file))
