import argparse
import os 
from test import test
from examples.flowers import flowers 

if __name__ == "__main__":
    examples_folder = os.path.join(os.getcwd(),"examples")
    examples = [example for example in os.listdir(examples_folder) if os.path.isdir(os.path.join(examples_folder,example))]
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--example", default="test",help="Choose an example [folder name] from the examples folder. By default it will run the 'test.py'",type=str)
    args = parser.parse_args()
    if args.example == "flowers":
        flowers.run()
    else:
        test()
    
