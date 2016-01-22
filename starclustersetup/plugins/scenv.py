import os

from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class EnvarPlugin(ClusterSetup):
    """
    Plugin that configures environment variables for a cluster
    """
    #vars_hash = {}
    var_str = ""
    envar_location = None
    def __init__(self, var_list=None,var_file=None,user_envar_location=None):
        en_vars = []
        if not var_list is None:
            en_vars = var_list.split(',')
        elif not var_file is None:
            log.info("Adding vars from: %s " % var_file)
            vfile_name = os.path.expanduser(var_file or '') or None
            if vfile_name is not None: 
                fh = open(vfile_name,"r")
                line = fh.readline()
                while not line == "":
                    en_vars.append(line.replace('\n',''))
                    line = fh.readline()
                fh.close()
        for var in en_vars:
            split_index = var.find('=')
            if not split_index == -1:
                #self.vars_hash[var[0:split_index]] = var[split_index:]
                self.var_str += 'export '+var[0:split_index]+'="'+var[split_index+1:].replace('"','\"')+'";\n'
        #log.info("VarCMD %s " % self.var_str)
        self.envar_location = user_envar_location
    def run(self, nodes, master, user, user_shell, volumes):
        if not self.var_str == "":
            for node in nodes:
                log.info("Adding vars to: %s " % node.alias)
                node.ssh.execute('echo \''+self.var_str.replace('\'', '\\\'')+'\' >> .bashrc')
                if self.envar_location is not None:
                    node.ssh.execute('echo \''+self.var_str.replace('\'', '\\\'')+'\' >> '+self.envar_location)

    def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        if not self.var_str == "":
            log.info("Adding vars to: %s " % node.alias)
            node.ssh.execute('echo \''+self.var_str+' >> .bashrc')
            if self.envar_location is not None:
                node.ssh.execute('echo \''+self.var_str.replace('\'', '\\\'')+'\' >> '+self.envar_location)

