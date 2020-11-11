import os
import json
import click
import time
import math
from pathlib import Path
from multiprocessing import Process
from instruction import Instruction
from custom_driver import CustomDriver
from devices import Devices
from dataclasses import asdict


def makeDir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def capture(instruction):
    output_dir = f'output/{instruction.title}'
    makeDir(output_dir)

    print(f'Started capture process...')

    driver = CustomDriver(instruction)

    driver.get(f'{instruction.base_url}')

    time.sleep(0.5) # Wait for the page finish to loading

    cookieBtn = driver.driver.find_element(by='css selector', value='#declineButton')
    cookieBtn.click()

    feedbackBtn = driver.driver.find_elements(by='css selector', value='.smcx-btn.smcx-btn-secondary.smcx-pull-left')[0]
    feedbackBtn.click()

    homeworkHelpBtn = driver.driver.find_elements(by='css selector', value='.membershipalert .nah')[0]
    homeworkHelpBtn.click()

    time.sleep(1) # Small time delay to let the modals fully close

    print(f'Beginning screenshot of {len(instruction.pages)} pages...')

    for page in instruction.pages:
        driver.get(f'{page}')

        driver.wait_and_see('#wrapper')

        fileLocation = page.replace(instruction.base_url, '').strip('/')
        saveLocation = f'{output_dir}/{fileLocation}.png'

        savePath, fileName = os.path.split(saveLocation)

        Path(savePath).mkdir(parents=True, exist_ok=True)

        try:
            driver.save_full_page_screenshot(saveLocation)
            print(f'Saved screenshot of [{fileLocation}]')
        except Exception:
            print(f'An error occurred when trying to screenshot [{fileLocation}]')

        time.sleep(0.5)


    driver.quit()

@click.command()
@click.argument('instruction_file')
def run(instruction_file):
    with open(instruction_file) as f:
        instruction_dict = json.load(f)
        instruction = Instruction.from_dict(instruction_dict)


    if (len(instruction.pages) <= 10):
        capture(instruction)
    else:
        processes = []
        chunkedPages = chunks(instruction.pages, math.ceil(len(instruction.pages) / 5))

        for chunk in chunkedPages:
            customInstruction = instruction
            customInstruction.pages = chunk

            p = Process(target=capture, args=(customInstruction,))
            p.start()
            processes.append(p)

        for process in processes:
            process.join()


if __name__ == '__main__':
    run()
