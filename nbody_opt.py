"""
    N-body simulation.

    Combined Optimizations
    Runtime: 28.307598999999755
    R = 101.76956199999995 / 28.307598999999755 = 3.595132247
"""
import itertools
import timeit

#Global Variables
PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
	'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

	'jupiter': ([4.84143144246472090e+00,
			-1.16032004402742839e+00,
			-1.03622044471123109e-01],
			[1.66007664274403694e-03 * DAYS_PER_YEAR,
			7.69901118419740425e-03 * DAYS_PER_YEAR,
			-6.90460016972063023e-05 * DAYS_PER_YEAR],
			9.54791938424326609e-04 * SOLAR_MASS),

	'saturn': ([8.34336671824457987e+00,
			4.12479856412430479e+00,
			-4.03523417114321381e-01],
			[-2.76742510726862411e-03 * DAYS_PER_YEAR,
			4.99852801234917238e-03 * DAYS_PER_YEAR,
			2.30417297573763929e-05 * DAYS_PER_YEAR],
			2.85885980666130812e-04 * SOLAR_MASS),

	'uranus': ([1.28943695621391310e+01,
			-1.51111514016986312e+01,
			-2.23307578892655734e-01],
			[2.96460137564761618e-03 * DAYS_PER_YEAR,
			2.37847173959480950e-03 * DAYS_PER_YEAR,
			-2.96589568540237556e-05 * DAYS_PER_YEAR],
			4.36624404335156298e-05 * SOLAR_MASS),

	'neptune': ([1.53796971148509165e+01,
			-2.59193146099879641e+01,
			1.79258772950371181e-01],
			[2.68067772490389322e-03 * DAYS_PER_YEAR,
			1.62824170038242295e-03 * DAYS_PER_YEAR,
			-9.51592254519715870e-05 * DAYS_PER_YEAR],
			5.15138902046611451e-05 * SOLAR_MASS)}
			
def advance(dt, iterations, bodies, body_pairs):
	for _ in range(iterations):
		for (body1, body2) in body_pairs:
			([x1, y1, z1], v1, m1) = bodies[body1]
			([x2, y2, z2], v2, m2) = bodies[body2]

			# Compute Deltas
			(dx, dy, dz) = (x1-x2, y1-y2, z1-z2)

			#update_vs compute_b(m2, dt, dx, dy, dz)
			mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
			m1_mag = m1 * mag
			m2_mag = m2 * mag
			
			v1[0] -= dx * m2_mag # m * Mag
			v1[1] -= dy * m2_mag
			v1[2] -= dz * m2_mag
			v2[0] += dx * m1_mag
			v2[1] += dy * m1_mag
			v2[2] += dz * m1_mag

		for body in bodies:
			(r, [vx, vy, vz], m) = bodies[body]

			#update_rs(r, dt, vx, vy, vz)
			r[0] += dt * vx
			r[1] += dt * vy
			r[2] += dt * vz
			
def report_energy(bodies, body_pairs, e=0.0):
	for (body1, body2) in body_pairs:
		((x1, y1, z1), v1, m1) = bodies[body1]
		((x2, y2, z2), v2, m2) = bodies[body2]

		(dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
		e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)

	for body in bodies:
		(r, [vx, vy, vz], m) = bodies[body]
		e += m * (vx * vx + vy * vy + vz * vz) / 2.

	return e

def nbody(loops, reference, iterations, bodies):
	'''
		nbody simulation
		loops - number of loops to run
		reference - body at center of system
		iterations - number of timesteps to advance
	'''

	#Offset momentum
	'''
		ref is the body in the center of the system
		offset values from this reference
	'''
	(px, py, pz) = (0.0, 0.0, 0.0)
	for body in bodies:
		(_, [vx, vy, vz], m) = bodies[body]
		px -= vx * m
		py -= vy * m
		pz -= vz * m

	(r, v, m) = bodies[reference]
	v[0] = px / m
	v[1] = py / m
	v[2] = pz / m
	
	body_pairs = list(itertools.combinations(bodies, 2))

	for i in range(loops):
		'''
			advance the system one timestep
		'''
		advance(0.01, iterations, bodies, body_pairs)
		
		print(report_energy(bodies, body_pairs))


if __name__ == '__main__':

	#Timing It
	print(timeit.timeit("nbody(100, 'sun', 20000, BODIES)", setup="from __main__ import BODIES,nbody", number=1))
