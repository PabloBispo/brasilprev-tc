import sys

from banco_imobiliario import run_game, show_stats


if __name__ == '__main__':
    args = sys.argv[1:]
    simulations = 300
    if len(args) > 0:
        try:
            simulations = int(args[0])
        except:
            pass
            
            
    stats = run_game(simulations = simulations)
    show_stats(stats)