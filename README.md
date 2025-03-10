# 2DPhysicsEngine
A Simple 2d physics engine in pygame

## circle class usage:

circle(loc_x, loc_y, radius) 
    // Initializes a circle object at position (loc_x, loc_y) with the specified radius.

draw(screen) 
    // Renders the circle on the provided Pygame surface.

update(x_inc, y_inc)
    // Moves the circle’s x-coordinate by x_inc and its y-coordinate by y_inc.


virtual_border class usage:

virtual_border(loc_x, loc_y, width, height)
    // Creates a rectangular border centered at (loc_x, loc_y) with the given width and height.

draw(screen)
    // Draws the rectangular border on the given Pygame surface.


physics_engine class usage:

physics_engine(gravity, friction, width, height)
    // Initializes the physics engine with the provided gravity, friction, and the screen dimensions.

manage_actor(actor, v_border, s_time)
    // Applies physics updates to the actor (circle) based on collisions with the border and screen edges,
    // incorporating gravity, friction, and reflection, using s_time (e.g., time.time()) to calculate elapsed time.
