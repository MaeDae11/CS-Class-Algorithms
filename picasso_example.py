import picasso

p = picasso.Picasso('Hello World')
p.add_point(0, 10)
p.add_point(1, 20)
p.add_point(2, 30)
p.add_point(3, 40)
p.export()

# p.draw_best_fitting_line = True