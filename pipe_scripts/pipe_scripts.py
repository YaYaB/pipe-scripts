import os
import sys
import argparse
import subprocess
import time

def get_args():
    parser = argparse.ArgumentParser(
        "Wait for scripts to finish before launching a pipe of scripts that will suceed to each other"
    )
    parser.add_argument("--waited_scripts", type=str, nargs='+')
    parser.add_argument("--future_scripts", type=str, nargs='+')
    args = parser.parse_args()
    return args


class Script:

    def __init__(self, name, type_of='bash'):
        # Name of the scripts
        self.name = name

        # Type of the script (bash or other)
        self.type = type_of

        # Get all the current PID
        self.pid = self.get_pids()

    def exist(self):
        # VERIFY if the scripts still exists
        self.pid = self.get_pids()
        if self.pid:
            return True
        else:
            return False

    def get_pids(self):
        try:
            pids = os.popen("pidof -x " + self.type + " " + self.name).read()
            if len(pids) != 0:
                pids = pids[:-1].split(' ')
        except:
            print('No pid was found associated to', self.type + ' ' + self.name, '. Script does not seem to be running')
            pids = []
        return pids


def remove_from_list(rm_list, indexes):
    # Get sort indexes in reverse way
    indexes.sort(reverse=True)

    for i in indexes:
        del rm_list[i]

    return rm_list


def main():
    args = get_args()
    waited_scripts = args.waited_scripts
    future_scripts = args.future_scripts
    
    # Create the list of scripts
    print('Waiting for the following script{} to finish:'.format('s' if len(waited_scripts) > 1 else ''))
    for script in waited_scripts:
        print('-', script)
    waited_scripts = [Script(x) for x in waited_scripts]
    while True:
        idx_to_delete = []
        for i, script in enumerate(waited_scripts):
            if not script.exist():
                print('Following script has finished:', script.name)                
                idx_to_delete.append(i)
        
        waited_scripts = remove_from_list(waited_scripts, idx_to_delete)
        # No more scripts to wait for
        if not waited_scripts:
            # We launch script from future_scripts and add it to waited_scripts
            now_script = future_scripts.pop(0)
            # The process will automaticaly wait but works only 
            # if script is launched from command not if it's a script that we
            # are waiting
            #subprocess.call(now_script, shell=True) 
            com = 'bash ' + now_script
            print('Launch following script:', com)
            subprocess.Popen(com, shell=True)            
            waited_scripts.append(Script(now_script))

            if not future_scripts:
                print('All scripts were executed')
                break
        
        time.sleep(10)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("Uncaught error waiting for scripts to finish")
        print(e)
        raise
