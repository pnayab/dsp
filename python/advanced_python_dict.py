Part III - Dictionary

Q6. Create a dictionary in the below format:
 
faculty_dict:

faculty_dict = {'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
                               ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
                     ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
                     ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']],
               'Parkar': [['Ph.D.', 'Associate Professor', 'new@mail.med.upenn.edu'],
                     ['Ph.D.', 'Professor', 'parkaar@upenn.edu']],
                'Parkar2':  [['Ph.D.', 'Associate Professor', 'new@mail.med.upenn.edu'],
                     ['Ph.D2.', 'Professor', 'parkaar@upenn.edu']]}

count = 1
for c in faculty_dict:
    if count <=3:
        print (c, faculty_dict[c])
        count += 1
        

Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
                  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
                  ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
                  ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

count = 1
for c in professor_dict:
    if count <=3:
        print (c, professor_dict[c])
        count += 1
        
Q8. It looks like the current dictionary is printing by first name. 
Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
                  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], 
                  ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
                  ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

count = 1
for c in sorted(professor_dict):
    if count <=3:
        print (c, professor_dict[c])
        count += 1
        
  



        
        
