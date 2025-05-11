def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    pizza.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    info.start_countdown(3)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

pizza: Sprite = None
scene.set_background_color(13)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . e e . . . . . e e e . . .
        . . e e e e . . . . e e e e . .
        . e e e e e e e e e e e e e e .
        . e e e e 1 1 e e 1 1 e e e e .
        . e e . e f 1 e e f 1 e . e e .
        . . . . e e e e e e e e . . . .
        . . . . e e e f f e e e . . . .
        . . . . e e e f f e e e . . . .
        . . . . e e e e e e e e . . . .
        . . . . . . . e e . . . . . . .
        . . . . . . f f f f . . . . . .
        . . . . e e e 5 e e e e . . . .
        . . . . e e e e e e e e . . . .
        . . . . e e e e e e e e . . . .
        . . . . e e e e e e e e . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(img("""
        . . . . . . b b b b . . . . . .
        . . . . . . b 4 4 4 b . . . . .
        . . . . . . b b 4 4 4 b . . . .
        . . . . . b 4 b b b 4 4 b . . .
        . . . . b d 5 5 5 4 b 4 4 b . .
        . . . . b 3 2 3 5 5 4 e 4 4 b .
        . . . b d 2 2 2 5 7 5 4 e 4 4 e
        . . . b 5 3 2 3 5 5 5 5 e e e e
        . . b d 7 5 5 5 3 2 3 5 5 e e e
        . . b 5 5 5 5 5 2 2 2 5 5 d e e
        . b 3 2 3 5 7 5 3 2 3 5 d d e 4
        . b 2 2 2 5 5 5 5 5 5 d d e 4 .
        b d 3 2 d 5 5 5 d d d 4 4 . . .
        b 5 5 5 5 d d 4 4 4 4 . . . . .
        4 d d d 4 4 4 . . . . . . . . .
        4 4 4 4 . . . . . . . . . . . .
        """),
    SpriteKind.food)