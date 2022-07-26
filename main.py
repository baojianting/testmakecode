def on_on_chat(num1):
    mobs.spawn(CHICKEN, pos(0, 0, 0))
player.on_chat("run", on_on_chat)

blocks.place(GRASS, pos(0, 0, 0))