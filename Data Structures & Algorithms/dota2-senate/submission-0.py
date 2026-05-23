class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sen = []
        R_present = 0
        D_present = 0
        for ch in senate:
            sen.append(ch)
            if ch == 'R':
                R_present += 1
            else:
                D_present += 1
        
        idx = 0
        R_count = 0
        D_count = 0
        while True:

            if sen[idx] == '0':
                if idx == len(sen) - 1:
                    idx = 0
                else:
                    idx += 1
                continue

            if sen[idx] == 'R':
                if R_count > 0:
                    sen[idx] = '0'
                    R_count -= 1
                    if idx == len(sen) - 1:
                        idx = 0
                    else:
                        idx += 1
                    continue

                if D_present == 0:
                    return "Radiant"
                else:
                    D_count += 1
                    D_present -= 1
            
            if sen[idx] == 'D':
                if D_count > 0:
                    sen[idx] = '0'
                    D_count -= 1
                    if idx == len(sen) - 1:
                        idx = 0
                    else:
                        idx += 1
                    continue

                if R_present == 0:
                    return "Dire"
                else:
                    R_count += 1
                    R_present -= 1

            if idx == len(sen) - 1:
                idx = 0
            else:
                idx += 1
        
