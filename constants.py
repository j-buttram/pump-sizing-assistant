
#minor loss coefficients
fitting = { 
    "threaded" : {"tee_thru" : 0.9, "tee_branch" : 2.0, "union" : 0.08, "elbow_reg_90" : 1.5, "elbow_reg_45" : 0.4, "elbow_lr_90" : 0.7, "return_180" : 1.5},
    "flanged" : {"tee_thru" : 0.2, "tee_branch" : 1.0, "elbow_reg_90" : 0.3, "elbow_lr_45" : 0.4, "elbow_lr_90" : 0.2, "return_180" : 0.2},
    }

valve = {
    "globe" : {"full_open" : 10},
    "angle" : {"full_open" : 2},
    "gate" : {"full_open" : 0.15, "1/4 closed" : 0.26, "1/2 closed" : 2.1, "3/4 closed" : 17},
    "check" : {"swing" : 2},
    "ball" : {"full_open" : 0.05, "1/3 closed" : 5.5, "2/3 closed" : 200},
    "diaphram" : {"full_open" : 2.3, "1/2 closed" : 4.3, "3/4 closed" : 21},
    "other" : {"water_meter" : 7}
}



#declarations   