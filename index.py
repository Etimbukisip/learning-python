from function import  describe_student as ds
students = {
     'name':'thompson','age':25,'girls':['joy','lucy','vera'], 'program':'python'
 }

#name_of_girlfriends(students['girls'][:1])
ds(students['name'],students['age'], students['program'])