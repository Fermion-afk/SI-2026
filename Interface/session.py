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
            "uni"    : None,   
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
    if ses["bas"]["status"] != "Not Created":
        ses["bas"]["bas"] = None
        ses["bas"]["status"] = "Outdated"

def invalidate_ham():
    if ses["ham"]["status"] != "Not Created":
        ses["ham"]["mat"] = None
        ses["ham"]["status"] = "Outdated"    

def invalidate_ep():
    if ses["ep"]["status"] != "Not Created":
        ses["ep"]["evals"] = None
        ses["ep"]["evecs"] = None
        ses["ep"]["status"] = "Outdated"        

def sys_ready():
    if (ses["sys"]["n"] is not None and
        ses["sys"]["k"] is not None and
        ses["sys"]["per"] is not None and
        ses["sys"]["uni"] is not None):
        ses["sys"]["status"] = "Configured"
    else:
        ses["sys"]["status"] = "Not Configured"

def par_ready():    
    mod = ses["mod"]["name"]
    if mod == "Huckel":
        if (ses["par"]["a"] is not None and
            ses["par"]["b"] is not None):

            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"
    elif mod == "Hubbard":
        if (ses["par"]["a"] is not None and
            ses["par"]["b"] is not None and
            ses["par"]["u"] is not None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"

    elif mod == "Extended Hubbard":
        if (ses["par"]["a"] is not None and
            ses["par"]["b"] is not None and
            ses["par"]["u"] is not None and
            ses["par"]["v"] is not None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"
    elif mod == "PPP":
        if (ses["par"]["a"] is not None and
            ses["par"]["b"] is not None and
            ses["par"]["u"] is not None and
            ses["par"]["v"] is not None):
            ses["par"]["status"] = "Complete"
        else:
            ses["par"]["status"] = "Incomplete"
    else:
        ses["par"]["status"] = "Incomplete"

def bas_ready():
    if (ses["bas"]["bas"] is not None):
        ses["bas"]["status"] = "Created"

def ham_ready():
    if ses["ham"]["mat"] is not None:
        ses["ham"]["status"] = "Ready"

def ep_ready():
    if (ses["ep"]["evals"] is not None and 
        ses["ep"]["evecs"] is not None):
        ses["ep"]["status"] = "Ready"
