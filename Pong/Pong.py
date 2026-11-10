import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# A rectangle defined by: x, y, width and height
paddle = pygame.Rect(30, 250, 15, 100)
paddle_speed = 350 #pixels per second

ball = pygame.Rect(390, 290, 20, 20)
ball_position = pygame.Vector2(ball.center)
ball_velocity = pygame.Vector2(-300, 200) #pixels per second

running = True

while running:
    # Time since the previous frame, measured in seconds
    dt = clock.tick(60) / 1000 #Limit the game to 100 frames per second


    # Handle input and window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Check which keys are currently held down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle.y -=round(paddle_speed * dt)

    if keys[pygame.K_s]:
        paddle.y += round(paddle_speed * dt)

    # Keep the paddle inside the window
    paddle.clamp_ip(screen.get_rect())

    # Move the ball, keeping its position in decimal precision
    ball_position += ball_velocity * dt
    ball.center = (round(ball_position.x), round(ball_position.y))

    # Bounce of the top and bottom walls
    if ball.top <=0 and ball_velocity.y < 0:
        ball.top = 0
        ball_velocity.y *= -1
        ball_position.y = ball.centery

    elif ball.bottom >= screen.get_height() and ball_velocity.y > 0:
        ball.bottom = screen.get_height()
        ball_velocity.y *= -1
        ball_position.y = ball.centery

    # Bounce off the paddle when travelling left.
    if ball.colliderect(paddle) and ball_velocity.x < 0:
        ball.left = paddle.right
        ball_velocity.x *= -1
        ball_position.x = ball.centerx

    # Reset the ball when it leaves either side of the screen
    if ball.right < 0 or ball.left > screen.get_width():
        ball_position.update(400, 300)
        ball.center = (400, 300)
        ball_velocity.update(-300, 200)

   # Draw the background
    screen.fill((20, 20, 30))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
   #Show the completed frame
    pygame.display.flip()


pygame.quit()