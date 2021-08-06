
class Responses:

    def __init__(self, input_file):
        self._input_file = input_file
        self._responses = {}
        
    @property
    def file(self): 
        return self._input_file

    @property
    def responses(self):
        return self._responses

    def read(self):
        # Read the content of the input file and populate the responses 
        # dictionary variable instance above. Use the responses as keys and 
        # categories as values

        with open(self.file) as f:
            lines = f.readlines()
            for line in lines:
                response, category = line.split(':')
                response = response.strip()
                category = category.strip()
                self._responses[response] = category

        return self.responses

    def display(self):
        # Sort magic8 responses in alphabetical order and display then on the screen. 
        # Call this function in your main loop for menu option b
        self._sort()

    def _sort(self):
        # Converts the dictionary to a list of tuples.
        # Loops over the list and uses a bubble sort to sort in ascending order
        # by the response value

        unsorted_list = [(k, v) for k, v in self.responses.items()]
            
        list_len = len(unsorted_list)

        for i in range(list_len - 1):
            for j in range(0, list_len - i - 1):
                if unsorted_list[j] > unsorted_list[j + 1]:
                    unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

        for i in unsorted_list:
            print(i)

    def write(self):
        # this function should write the responses to user supplied output file
        # prompt the user to enter file name then dump the content of responses
        # to the file
        output_file = input('Enter the name of an output file'
                            ' to write responses to: ')
        file_out = open(output_file, 'w')
        for response in self._responses:
            print(response, ":", self._responses[response], file=file_out)
        file_out.close()

    def add(self):
        # Extra credit 
        # Update the responses container. i.e. prompt the user to enter a new response 
        # and its category. Add the response to the dictionary
        response = input('Enter a new response for the Magic 8 Ball: ')
        category = input('Enter the corresponding category for your response: ')
        self._responses[response] = category

