def RQA(recurrence_matrix):
  r_rate = recurrence_rate(recurrence_matrix)
  print("Recurrence rate: ", r_rate)

  lmax = LMAX(recurrence_matrix)
  print("Lmax: ", lmax)

  lmin = LMIN(recurrence_matrix)
  print("Lmax: ", lmin)

  deter = determinism(recurrence_matrix, lmin)
  print("Determinism: ", deter)

  lam = LAM(recurrence_matrix)
  print("Laminarity: ", lam)

  tt = TT(recurrence_matrix)
  print("Trapping time: ", tt)

  shan = ShanEn(recurrence_matrix, lmin)
  print("Shannon Entropy: ", shan)
  
#####

def recurrence_analysis(rr_intervals, d=1, tau=1, threshold=1):
  recurrence_matrix = recurrence_plot(rr_intervals, d, tau, threshold)
  rqa = RQA(recurrence_matrix)
