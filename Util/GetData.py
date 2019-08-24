


user_id = 792935


so = StackAPI('stackoverflow')

me = so.user(user_id)
answers = me.answers.fetch()