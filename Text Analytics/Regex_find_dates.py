import re
from calendar import month_name
import sys

def main(filename):
    """This function takes in a txt input news article,
    looks for the defined date patterns, and output the dates
    for evaluation.

    Input: 
    	filename: txt filename
    Returns: 
    	dates_found: extracted date types
    """
    print ("\nreading in txt file...\n")
    readin = open(filename, 'r').read()
    lines = []

    print ("splitting sentences...\n")
    lines = readin.split("\n\n")

    # Create list of all the months, weekdays, end strings, and timing of the day
    fullmonth = []
    for i in month_name:
        if bool(i):
            fullmonth.append(i)
    short_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Sept', 'Oct', 'Nov', 'Dec']
    month = fullmonth + short_month
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    timing = ['afternoon', 'morning', 'evening']
    end_string = ['am', 'pm', 'AM', 'PM', 'a.m.', 'p.m.', 'st', 'nd', 'rd', 'th']

    print ("compiling date patterns\n")

    # 1/8/2019, 01/08/2019, 1-8-2019, 01-08-2019
    p1 = re.compile(r'\b\d?\d[-\/]\d?\d[-\/][1-9]\d(?:\d{2})?\b') 

    # Oct.8, 2018
    p2 = re.compile(r'\b(?:%s)\.?[ ]\d?\d[,][ ][1-9]\d(?:\d{2})?\b' % '|'.join(month)) 

    # Monday, 8am or Monday the 23rd
    p3 = re.compile(r'(%s)(\s|,\s)[a-z]*\s?\d?\d(%s)' % ('|'.join(weekday), '|'.join(end_string))) 

    # Wednesday, Oct. 11th OR Tuesday, Oct. 2018
    p4 = re.compile(r'(%s)(,\s)(?:%s)[.\s][ ]\d?\d((th)|(\d{3}))' % ('|'.join(weekday), '|'.join(month)))

    # Monday(,\s)afternoon
    p5 = re.compile(r'(%s)(\s|,\s)(%s)' % ('|'.join(weekday), '|'.join(timing)), re.I)

    # Oct 20th
    p6 = r'\b(%s)(?:-|\.|\s|,)\d{1,2}(%s)?\b' % ('|'.join(month), '|'.join(end_string))

    # Holiday
    holiday = re.compile(r'\b(?:[A-Z][a-z]*\b\s*)+\s[dD]ay')

    # Pure weekdays not followed by endings, not Monday 8a.m.
    pure_wkd_1 = re.compile(r'(%s)(?![ ]%s|\s?\d?\d(%s)|(,\s)(?:%s)[.\s][ ]\d?\d((th)|(\d{3})))' % ('|'.join(weekday), '|'.join(timing), '|'.join(end_string),'|'.join(month)),re.I)

    # Store extracted dtypes to output
    dates_found=[]

    count = 0
    #Loop through each sentence to look for the date types
    for sent in lines:
        count+=1
        
        dtype1 = re.finditer(p1, sent)
        if dtype1:
            for d in dtype1:
                dates_found.append(sent[d.start():d.end()])
        
        dtype2 = re.finditer(p2, sent)
        if dtype2:
            for d in dtype2:
                dates_found.append(sent[d.start():d.end()])

        dtype3 = re.finditer(p3, sent)
        if dtype3:
            for d in dtype3:
                dates_found.append(sent[d.start():d.end()])
        
        dtype4 = re.finditer(p4, sent)
        if dtype4:
            for d in dtype4:
                dates_found.append(sent[d.start():d.end()])
        
        dtype5 = re.finditer(p5, sent)
        if dtype5:
            for d in dtype5:
                dates_found.append(sent[d.start():d.end()])
        
        dtype6 = re.finditer(p6, sent)
        if dtype6:
            for d in dtype6:
                dates_found.append(sent[d.start():d.end()])
                
        holiday_type = re.finditer(holiday, sent)
        if holiday_type:
            for d in holiday_type:
                dates_found.append(sent[d.start():d.end()])
        
        # Extract pure weekdays
        wkd1 = re.finditer(pure_wkd_1, sent)
        if wkd1:
            for d in wkd1:
                dates_found.append(sent[d.start():d.end()])
        
        
        # Check results by line
        #print(count, dates_found) #check results by line
                
    return dates_found

if __name__ == "__main__":
    filename = sys.argv[1]
    print("\nReading in: ", filename)
    out = main(filename)

    # Output extracted date types
    with open('dates_output.txt', 'w') as f:
    	for item in out:
    		f.write("%s\n" % item)
    print("Finished outputting dates found.\n")


