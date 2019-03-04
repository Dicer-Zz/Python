import numpy as np 
import matplotlib.pyplot as plt 

class GameOfLife():

	def __init__(self, cell_shape = (20, 20), cells = None):
		self.cells = np.zeros(cell_shape, dtype = 'i1')
		real_width = cell_shape[0] - 2;
		real_heigth = cell_shape[1] - 2;
		if cells is None:
			self.cells[1:-1, 1:-1] = np.random.randint(0, 2, size = (real_width, real_heigth))
		else:
			self.cells = cells
		self.iter = 0

	def _updata(self):
		tmp = np.zeros(self.cells.shape, dtype = 'i1')
		cells = self.cells 
		for i in range(1, cells.shape[0]-1):
			for j in range(1, cells.shape[1]-1):
				neighbor = cells[i-1:i+2, j-1:j+2].reshape(-1)
				neighbor_sum = np.sum(neighbor == 1) - cells[i, j]
				if neighbor_sum == 3:
					tmp[i, j] = 1
				elif neighbor_sum == 2:
					tmp[i, j] = cells[i, j]
				else:
					tmp[i, j] = 0
		self.cells = tmp
		self.iter += 1

	def run(self, lim):
		plt.ion()
		while self.iter < lim:
			plt.title('Iter {}'.format(self.iter))
			plt.imshow(self.cells)
			self._updata()
			plt.pause(0.01)
		plt.ioff()

if __name__ == '__main__':
	gol = GameOfLife(cell_shape = (30, 30))
	gol.run(300)