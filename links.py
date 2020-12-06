import os
import json
import click
import time
from multiprocessing import Process
from instruction import Instruction
from custom_driver import CustomDriver
from dataclasses import asdict

def makeDir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def links(instruction):
    output_dir = f'output/{instruction.title}'
    makeDir(output_dir)

    driver = CustomDriver(instruction)
    pages = []

    count = 0
    num_levels = len(instruction.levels)

    print(f'Starting to collect links ({num_levels})')

    for level in instruction.levels:
        url = f'{instruction.base_url}{level}'

        driver.get(url)

        links = driver.find_elements('#content .sub_navigation a')

        if (len(links) == 0):
            pages.append(url)

        for link in links:
            pages.append(link.get_attribute('href'))

        count += 1
        print(f'Found {len(links)} links for [{level}]. Completed: [{count}/{num_levels}]')

        time.sleep(0.2)

    driver.quit()

    with open(f'{output_dir}/pages.json', 'a') as out:
        out.write(json.dumps(pages, indent=2) + '\n')

@click.command()
@click.argument('instruction_file')
def run(instruction_file):
    with open(instruction_file) as f:
        instruction_dict = json.load(f)
        instruction = Instruction.from_dict(instruction_dict)

    links(instruction)

if __name__ == '__main__':
    run()
