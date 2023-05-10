import introstory

def exposite(text:tuple):
    for paragraph in text:
    # if not the last paragraph, add a ... (press enter to continue)
        if paragraph != text[-1]:
            input(paragraph + " \n\033[3m\033[92mPress enter to continue...\033[0m")
        else:
            input(paragraph)



if __name__ == "__main__":
    exposite(introstory.introduction)