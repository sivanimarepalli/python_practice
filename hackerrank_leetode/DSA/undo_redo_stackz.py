# Implement a simple text editor’s Undo/Redo using stacks.
def text_editor(undo_stack,redo_stack,operation):
    if operation=="add text":
        if undo_stack:
            prev_text=undo_stack[-1]
        else:
            prev_text=""

        new_text=input()
        curr_text=prev_text+new_text
        undo_stack.append(curr_text)
        redo_stack.clear()
        return curr_text
    if operation=="undo":
        if undo_stack:
            last_state=undo_stack.pop()
            redo_stack.append(last_state)
            if undo_stack:
                return undo_stack[-1]
            else:
                return ""
    if operation=="redo":
        if redo_stack:
            p_state=redo_stack.pop()
            undo_stack.append(p_state)
            if undo_stack:
                return undo_stack[-1]
            else:
                return ""

s1=[]
s2=[]
call=text_editor(s1,s2,"add text")
call1=text_editor(s1,s2,"undo")
call2=text_editor(s1,s2,"redo")
print(call)
print(call1)
print(call2)
        
    