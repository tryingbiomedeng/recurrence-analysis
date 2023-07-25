def recurrence_rate(recurrence_matrix):
  N = recurrence_matrix.shape[0]
  rec_count = 0

  for i in range(N):
    for j in range(N):
      if recurrence_matrix[i,j] == 1:
        rec_count += 1

  return rec_count / (N**2)

#####

def LMAX(R):
  L = []
  N = R.shape[0]
  for i in range(N):
    l = 0
    for j in range(N-i):
        if R[i+j,j] == 1:
            l += 1
        else:
            break
    L.append(l)
  return max(L)

#####

def LMIN(R):
  L = []
  N = R.shape[0]
  for i in range(N):
    l = 0
    for j in range(N-i):
      if R[i+j,j] == 0:
        l += 1
      else:
        break
    L.append(l)
  return min(L)

#####

def LMEAN(LMIN, LMAX):
  L = (LMIN + LMAX) / 2
  return L

#####

def determinism(recurrence_matrix, lmin):
  N = len(recurrence_matrix)

  hist = np.zeros(N+1) # histogram of diagonal line lengths

  for i in range(N):
    for j in range(N):
      if recurrence_matrix[i,j] == 1:
        l = 1
        while (i+l < N) and (j+l < N) and recurrence_matrix[i+l, j+l] == 1:
          l += 1
        if l >= lmin:
          hist[l] += 1

  l = np.arange(lmin, N).reshape(-1,1) # diagonal lengths
  P = hist[lmin:] / np.sum(hist[lmin:]) # probability of each length

  det = np.sum(l * P) / np.sum(recurrence_matrix)

  return det

#####

def LAM(R):

  # R is the recurrence matrix

  N = len(R)

  hist = np.zeros(N) # histogram of vertical line lengths

  for i in range(N):
    for j in range(N):
      if R[i,j] == 1:
        v = 1
        while (i+v < N) and (R[i+v,j] == 1):
          v += 1
        hist[v] += 1

  v = np.arange(1, N).reshape(-1,1) # vertical lengths
  P = hist / np.sum(hist) # probability of each length

  lam = np.sum(v * P[1:]) / np.sum(v * P)

  return lam

#####

def TT(R):
  N = R.shape[0]
  P = np.zeros(N)
  for i in range(N):
    l = 0
    for j in range(N-i):
      if R[i+j,j] == 1:
        l += 1
      else:
        break
    P[l-1] += 1
  P = P/P.sum()
  vmin = np.where(P > 0)[0][0] + 1
  TT = 0
  denom = 0
  for v in range(vmin, N+1):
    TT += v * P[v-1]
    denom += P[v-1]
  if denom > 0:
    TT /= denom
  else:
    TT = np.nan

  return TT

#####

def ShanEn(R, lmin):
  N = R.shape[0]
  P = np.zeros(N)
  for i in range(N):
    l = 0
    for j in range(N-i):
      if R[i+j,j] == 1:
        l += 1
      else:
        break
    P[l-1] += 1
  P = P/P.sum()
  ShanEn = 0
  for l in range(lmin, N+1):
    p_l = P[l-1]
    if p_l > 0:
      ShanEn += p_l * np.log(p_l)
  ShanEn = -ShanEn

  return ShanEn
