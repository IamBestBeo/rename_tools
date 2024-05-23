import maya.cmds as cmds

def sequence_renamer():
    selection = cmds.ls(selection=True)
    dialog = cmds.promptDialog(title=("Sequence renamer"), message="Enter name. Optional: Add {} to be replaced by the number", button=["Rename", "Cancel"], defaultButton="Rename", cancelButton="Cancel", dismissString="Cancel")
    if dialog == "Rename":
        name = cmds.promptDialog(query=True, text=True)
        number = len(selection)
        if len(selection) >= 2:
            for item in selection[::-1]:
                padding = 3
                newNumber = str(number).rjust(padding, "0")
                if "{}" in name:
                    cmds.rename(item, (name.replace("{}", newNumber)))
                else:
                    cmds.rename(item, (name + newNumber))
                number = number - 1
        else:
            cmds.rename(selection[0], name)
import maya.cmds as cmds

def add_prefix(*args):
    prefix = cmds.textField('prefixTextField', query=True, text=True)
    selection = cmds.ls(selection=True)
    
    if not prefix:
        cmds.warning("Please enter a prefix")
    elif not selection:
        cmds.warning("Please select objects to rename")
    else:
        for item in selection[::-1]:
            cmds.rename(item, (prefix + item))

def add_suffix(*args):
    suffix = cmds.textField('suffixTextField', query=True, text=True)
    selection = cmds.ls(selection=True)
    
    if not suffix:
        cmds.warning("Please enter a suffix")
    elif not selection:
        cmds.warning("Please select objects to rename")
    else:
        for item in selection[::-1]:
            object_split = item.split("|")
            new_item = object_split[-1]
            cmds.rename(item, (new_item + suffix))

def rename_by_type(*args):
    selection = cmds.ls(selection=True)
    for item in selection[::-1]:
        # Find object type (check if shape or transform)
        try:
            format = cmds.listRelatives(item)
            format = cmds.objectType(format[0])
        except:
            format = cmds.objectType(item)

        if format == "clusterHandle":
            typeName = "CLU"
        elif format == "ikEffector":
            typeName = "IKE"
        elif format == "ikHandle":
            typeName = "IKH"
        elif format == "joint":
            typeName = "JNT"
        elif format == "mesh":
            typeName = "GEO"
        elif format == "nurbsCurve":
            typeName = "CURVE"
        elif format == "transform":
            typeName = "GRP"
        elif format == "follicle":
            typeName = "FOLL"
        elif format == "camera":
            typeName = "CAM"
        elif format == "locator":
            typeName = "LOC"
        elif format == "multiplyDivide":
            typeName = "MULT"
        elif format == "plusMinusAverage":
            typeName = "SUM"
        elif format == "weightDriver":
            typeName = "DRIVER"
        elif format == "reverse":
            typeName = "REV"
        elif format == "condition":
            typeName = "CON"
        elif format == "remapValue":
            typeName = "REMAP"
        elif format == "blinn" or format == "phong" or format == "VRayMtl":
            typeName = "MAT"
        elif format == "nurbsSurface":
            typeName = "NURBS"
        elif format == "dynamicConstraint":
            typeName = "CONS"
        elif format == "skinCluster":
            typeName = "BIND"
        else:
            typeName = str(format).translate({ord(c): None for c in 'aeiouAEIOU'}).upper()
            typeName = typeName[0:4]
            print("Auto converted name used for '{}'".format(format))

        if typeName != "undefined":
            if typeName not in item.split("|")[-1]:
                cmds.rename(item, (item.split("|")[-1] + "_" + typeName))
        else:
            print(typeName)
            print(format)
            
            



def sequence_renamer(dummy_arg):  
    selection = cmds.ls(selection=True)
    dialog = cmds.promptDialog(title=("Sequence renamer"), message="Name Sequence = Object name + 00X. Where X is an integer from 1 to infinity", button=["Rename", "Cancel"], defaultButton="Rename", cancelButton="Cancel", dismissString="Cancel")
    if dialog == "Rename":
        name = cmds.promptDialog(query=True, text=True)
        number = len(selection)
        if len(selection) >= 2:
            for item in selection[::-1]:
                padding = 3
                newNumber = str(number).rjust(padding, "0")
                if "{}" in name:
                    cmds.rename(item, (name.replace("{}", newNumber)))
                else:
                    cmds.rename(item, (name + newNumber))
                number = number - 1
        else:
            cmds.rename(selection[0], name)


def add_prefix(*args):
    prefix = cmds.textField('prefixTextField', query=True, text=True)
    selection = cmds.ls(selection=True)
    
    if not prefix:
        cmds.warning("Please enter a prefix")
    elif not selection:
        cmds.warning("Please select objects to rename")
    else:
        for item in selection[::-1]:
            cmds.rename(item, (prefix + item))
    
    
    cmds.textField('prefixTextField', edit=True, text='')

def add_suffix(*args):
    suffix = cmds.textField('suffixTextField', query=True, text=True)
    selection = cmds.ls(selection=True)
    
    if not suffix:
        cmds.warning("Please enter a suffix")
    elif not selection:
        cmds.warning("Please select objects to rename")
    else:
        for item in selection[::-1]:
            object_split = item.split("|")
            new_item = object_split[-1]
            cmds.rename(item, (new_item + suffix))
    
    
    cmds.textField('suffixTextField', edit=True, text='')

def RN_UI():
    # Check if the window already exists
    if cmds.window('renameWindow', exists=True):
        cmds.deleteUI('renameWindow')

    # Create the window
    window = cmds.window('renameWindow', title='Rename Tools', widthHeight=(350, 150))

    # Create a form layout
    form = cmds.formLayout()

    # First row for prefix
    prefix_field = cmds.textField('prefixTextField', placeholderText='Prefix_____')
    prefix_button = cmds.button(label='Add Prefix', command=add_prefix)

    # Second row for suffix
    suffix_field = cmds.textField('suffixTextField', placeholderText='_____Suffix')
    suffix_button = cmds.button(label='Add Suffix', command=add_suffix)

    # Third row for renaming by type
    rename_button = cmds.button(label='Rename by Type', command=rename_by_type)

    # Fourth row for sequence renamer
    sequence_renamer_button = cmds.button(label='Sequence Renamer', command=lambda dummy_arg: sequence_renamer(dummy_arg))

    # Attach controls to form layout
    cmds.formLayout(form, edit=True,
                    attachForm=[(prefix_field, 'top', 5), (prefix_field, 'left', 5), (prefix_field, 'right', 5),
                                (prefix_button, 'top', 5), (prefix_button, 'right', 5),
                                (suffix_field, 'left', 5), (suffix_field, 'right', 5),
                                (suffix_button, 'right', 5),
                                (rename_button, 'left', 5), (rename_button, 'right', 5),
                                (sequence_renamer_button, 'left', 5), (sequence_renamer_button, 'right', 5)],
                    attachControl=[(suffix_field, 'top', 5, prefix_field),
                                   (suffix_button, 'top', 5, prefix_button),
                                   (rename_button, 'top', 5, suffix_field),
                                   (sequence_renamer_button, 'top', 5, rename_button)],
                    attachPosition=[(prefix_field, 'right', 5, 75), (suffix_field, 'right', 5, 75)])

    # Show the window
    cmds.showWindow(window)

# Run the UI creation function
RN_UI()
