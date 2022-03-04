def do_iterative_refinement(map_3d_init, particles):
	"""
	Performs interative refimenent in a Bayesean expectation maximization setting,
	i.e. maximum a posteriori estimation.

	Input
	_________
	map_3d_init
		initial estimate
		input map
		shape (n_pix,n_pix,n_pix)
	particles
		particles to be reconstructed
		shape (n_pix,n_pix)

	
	Returns
	_________
	
	map_3d_final
		final updated map
		shape (n_pix,n_pix,n_pix)
	
	"""

	# split particles up into two half sets for statistical validation

	# align particles to 3D volume
		# decide on granularity of rotations
		# i.e. how finely the rotational SO(3) space is sampled in a grid search. 
		# see branch and bound

		def do_adaptive_grid_search(particle, map_3d):
			# a la branch and bound
			# not sure exactly how you decide how finely gridded to make it. 
			# perhaps heuristics based on how well the signal agrees in half_map_1, half_map_2 (Fourier frequency)
			

			def grid_SO3_uniform(n_rotations):
				"""
				uniformly grid (not sample) SO(3)
				can use some intermediate encoding of SO(3) like quaternions, axis angle, Euler
				final output 3x3 rotations
			
				"""
				rots = np.ones((n_rotations,3,3))
				return rots

			rots = grid_SO3()

			def do_bayesean_weights(particle, map_3d):

		bayesean_weights = do_adaptive_grid_search(particle, map_3d)
		

	for particle in particles:
		bayesean_weights = do_adaptive_grid_search(particle, map_3d)

		




