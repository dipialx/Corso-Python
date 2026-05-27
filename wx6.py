import wx


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(
            parent=None,
            title="wxPython Widgets Demo",
            size=(700, 600)
        )

        panel = wx.Panel(self)

        # ---------- STATIC TEXT ----------
        wx.StaticText(panel, label="Name:", pos=(20, 20))

        # ---------- TEXT INPUT ----------
        self.name_input = wx.TextCtrl(
            panel,
            pos=(120, 20),
            size=(100, 25)
        )

        # ---------- CHECKBOX ----------
        self.checkbox = wx.CheckBox(
            panel,
            label="I like Python",
            pos=(20, 70)
        )

        # ---------- RADIO BUTTONS ----------
        wx.StaticText(panel, label="Select Level:", pos=(20, 110))

        self.radio1 = wx.RadioButton(
            panel,
            label="Beginner",
            pos=(20, 140),
            style=wx.RB_GROUP
        )

        self.radio2 = wx.RadioButton(
            panel,
            label="Intermediate",
            pos=(150, 140)
        )

        # ---------- COMBO BOX ----------
        wx.StaticText(panel, label="Favorite Language:", pos=(20, 190))

        self.combo = wx.ComboBox(
            panel,
            choices=["Python", "JavaScript", "Java", "C++"],
            pos=(20, 220),
            size=(200, 25)
        )

        # ---------- LIST BOX ----------
        wx.StaticText(panel, label="Technologies:", pos=(20, 270))

        self.listbox = wx.ListBox(
            panel,
            choices=["Docker", "Redis", "FastAPI", "Django", "LLM"],
            pos=(20, 300),
            size=(200, 100)
        )

        # ---------- SLIDER ----------
        wx.StaticText(panel, label="Experience Level:", pos=(300, 20))

        self.slider = wx.Slider(
            panel,
            value=5,
            minValue=0,
            maxValue=10,
            pos=(300, 50),
            size=(250, -1)
        )

        # ---------- BUTTON ----------
        self.button = wx.Button(
            panel,
            label="Submit",
            pos=(300, 120),
            size=(120, 40)
        )

        self.button.Bind(wx.EVT_BUTTON, self.on_submit)

        # ---------- MULTILINE TEXT ----------
        wx.StaticText(panel, label="Output:", pos=(300, 190))

        self.output = wx.TextCtrl(
            panel,
            pos=(300, 220),
            size=(350, 180),
            style=wx.TE_MULTILINE
        )

        # ---------- NOTEBOOK (TABS) ----------
        notebook = wx.Notebook(panel, pos=(20, 430), size=(630, 120))

        tab1 = wx.Panel(notebook)
        tab2 = wx.Panel(notebook)

        wx.StaticText(tab1, label="This is Tab 1", pos=(20, 20))
        wx.StaticText(tab2, label="This is Tab 2", pos=(20, 20))

        notebook.AddPage(tab1, "Home")
        notebook.AddPage(tab2, "Settings")

        self.Show()

    def on_submit(self, event):
        name = self.name_input.GetValue().strip()
        language = self.combo.GetValue()
        tech = self.listbox.GetStringSelection()
        experience = self.slider.GetValue()

        errors = []

        if not name:
            errors.append("Name is required.")

        if len(name) < 2:
            errors.append("Name must contain at least 2 characters.")

        if not language:
            errors.append("Please select a favorite language.")

        if not tech:
            errors.append("Please select a technology.")

        if experience == 0:
            errors.append("Experience level must be greater than 0.")

        if errors:
            wx.MessageBox(
                "\n".join(errors),
                "Validation Error",
                wx.OK | wx.ICON_ERROR
            )
            return

        likes_python = self.checkbox.GetValue()

        if self.radio1.GetValue():
            level = "Beginner"
        else:
            level = "Intermediate"

        result = f"""
    Name: {name}
    Likes Python: {likes_python}
    Level: {level}
    Favorite Language: {language}
    Technology: {tech}
    Experience: {experience}
    """

        self.output.SetValue(result)

        wx.MessageBox("Form submitted successfully!")


app = wx.App()

frame = MyFrame()

app.MainLoop()