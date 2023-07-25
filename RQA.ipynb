def recurrence_plot(rr_intervals, d=1, tau=1, threshold=1):
  N = len(rr_intervals) - (d-1)*tau

  distances = np.zeros((N, N))

  for i in range(N):
    for j in range(N):
      xi = rr_intervals[i:i+d*tau:tau]
      xj = rr_intervals[j:j+d*tau:tau]

      distances[i, j] = np.linalg.norm(xi - xj)

  threshold = 10

  recurrence_matrix = np.zeros((N, N))

  for i in range(N):
    for j in range(N):
      if distances[i, j] <= threshold:
        recurrence_matrix[i, j] = 1

  print(recurrence_matrix)

  plt.figure(figsize=(6, 6))
  plt.imshow(recurrence_matrix, cmap='binary', origin='lower', vmin=0, vmax=1)
  plt.colorbar()
  plt.xlabel('Time (RR Intervals)')
  plt.ylabel('Time (RR Intervals)')
  plt.title('Recurrence Plot')
  plt.show()

  return recurrence_matrix
