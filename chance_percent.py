"""Percent of change"""
import faculty as fac
def chance_engineering():
    """chance of engineering"""
    percent = (fac.engineering(gat, pat1, pat3)/100)*100
    return percent

def chance_engineering_national():
    """chance of engineering national"""
    percent = (fac.engineering_national(gat1, gat2, pat1, pat3)/100)*100
    return percent

def chance_science():
    """chance of science"""
    percent = (fac.science(gat, pat1, pat2, branch)/100)*100
    return percent

def chance_architecture():
    """chance of architecture"""
    percent = (fac.architecture(gat, pat4, pat6, branch)/100)*100
    return percent

def chance_business():
    """chance of business"""
    percent = (fac.business_administration(gat, pat1)/100)*100
    return percent

def chance_information_technology():
    """chance of information techonology"""
    percent = (fac.information_technology(gat, pat1)/100)*100
    return percent

def chance_food_industry():
    """chance of food industry"""
    percent = (fac.food_industry(gat, pat1, pat2, branch)/100)*100
    return percent

def chance_education_industry_technology():
    """chance of education industry technology"""
    percent = (fac.education_industry_technology(gat, pat2, pat3, pat4, pat5, branch)/100)*100
    return percent

def chance_agricultural_technology():
    """chance of agricultural technology"""
    percent = (fac.agricultural_technology(gat85, pat1, pat2)/100)*100
    return percent

def chance_engineering_manufacturing():
    """chance of engineering manufacturing"""
    percent = (fac.engineering_manufacturing(pat1, pat2, pat3)/100)*100
    return percent

def chance_bachelor_technokmitl():
    """chance of bachelor technokmitl"""
    percent = (fac.bachelor_technokmitl(gat, pat1, pat2)/100)*100
    return percent

def chance_aviation_industry():
    """chance of aviation industry"""
    percent = (fac.aviation_industry(gat, gat2, pat1, pat3, branch)/100)*100
    return percent

def chance_imse():
    """chance of food imse"""
    percent = (fac.imse(gat, pat1, pat3)/100)*100
    return percent

def chance_kmitl_pcc():
    """chance of kmitl pcc"""
    percent = (fac.kmitl_pcc(gat, pat1, pat2, pat3, faculty)/100)*100
    return percent
