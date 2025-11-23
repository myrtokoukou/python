# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 19:45:29 2025

@author: myrto
"""

sunolo_misthwn = sunolo_krathsewn = 0

for upallilos in range(180):
    epipedo_morfwshs = input('Επίπεδο μόρφωσης(ΥΕ,ΜΕ,ΑΕ):')
    proipiresia = int(float(input('Χρόνια Προυπηρεσίας:')))
    if epipedo_morfwshs == 'ΥΕ':
        if proipiresia <= 10:
            misthos = 570
        else:
            misthos = 690
    elif epipedo_morfwshs == 'ΜΕ':
        if proipiresia <= 10:
            misthos = 680
        else:
            misthos = 990
    elif epipedo_morfwshs == 'ΑΕ':
        if proipiresia <= 10:
            misthos = 790
        else:
            misthos = 1300
    xronoepidoma = (proipiresia//3)*(8/10)*misthos
    krathseis = (misthos+xronoepidoma)*(20/100)
    katharosmisthos = misthos+xronoepidoma-krathseis
    print(xronoepidoma, krathseis, katharosmisthos)
    sunolo_misthwn += misthos+xronoepidoma
    sunolo_krathsewn += krathseis
print(sunolo_krathsewn,sunolo_misthwn)
        
                
            
        
    
    