from sumatra.projects import load_project
proj = load_project()

# Either of the following two lines will
# cause the bug to be triggered below.
proj.record_store.list('SumatraBug')
#proj.get_record('20140420-185235')  # use any valid Sumatra label

proj = load_project()  # triggers the exception
