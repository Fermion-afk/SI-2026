ses = {}

def init():
    global ses
    ses = {
        "mod" : {
            "name" : None
        },
        "sys" : {
            "n"      : None,
            "k"      : None,
            "per"    : None,
            "c"      : None, 
            "coords" : None,
            "dis_mat" : None,
            "status" : "Not Configured"
        },
        "par" : {
            "a"   : None,
            "b"   : None,
            "u"   : None,
            "v"   : None,
            "status" : "Not configured"
        },
        "bas" : {
            "bas" : None,
            "status" : "Not Created"
        },
        "ham" : {
            "mat"    : None,
            "status" : "Not Created"
        },
        "ep" : {
            "evals"  : None,
            "evecs"  : None,
            "status" : "Not Created"
        }
    }

def invalidate_bas():
    ses["bas"]["status"] = "outdated"

def bas_ready():
    ses["bas"]["status"] = "Created"

def invalidate_ham():
    if ses["ham"]["status"] == "Not Created":
        ses["ham"]["mat"] = None
        ses["ham"]["evals"] = None
        ses["ham"]["evecs"] = None
        ses["ham"]["status"] = "Outdated"
        ses["ham"]["diag"] = None

def ham_ready():
    ses["ham"]["status"] = "Ready"

def sys_ready():
    if (ses["sys"]["n"] is not None and
        ses["sys"]["k"] is not None and
        ses["sys"]["per"] is not None):
        ses["sys"]["status"] = "Configured"

def par_ready():    
    mod = ses["mod"]["name"]
    if mod == "Huckel":
        if (ses["par"]["a"] != None and
            ses["par"]["b"] != None):

            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"
    elif mod == "Hubbard":
        if (ses["par"]["a"] != None and
            ses["par"]["b"] != None and
            ses["par"]["u"] != None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"

    elif mod == "Extended Hubbard":
        if (ses["par"]["a"] != None and
            ses["par"]["b"] != None and
            ses["par"]["u"] != None and
            ses["par"]["v"] != None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"
    elif mod == "PPP":
        if (ses["par"]["a"] != None and
            ses["par"]["b"] != None and
            ses["par"]["u"] != None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"

def ep_ready():
    if (ses["ep"]["evals"] is not None and 
        ses["ep"]["evecs"] is not None):

        ses["ep"]["status"] = "Ready"

def invalidate_ep():
    ses["ep"]["evals"] = None
    ses["ep"]["evecs"] = None
    ses["ep"]["status"] = "Outdated"