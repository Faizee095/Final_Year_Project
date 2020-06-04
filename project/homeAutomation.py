from src.services.startUp.startUp import main
from src.services.onInit.setup import onInit

if __name__ == '__main__':
    onInit()
    print("System OK")
    main()
