import streamlit as st
import numpy as np
import time

def sidebar():
    with st.sidebar:
        st.sidebar.subheader("Sidebar")
        st.code(
            """
            with st.sidebar:
                st.sidebar.subheader("Sidebar")
                # Using object notation
                add_selectbox = st.sidebar.selectbox(
                    "How would you like to be contacted?",
                    ("Email", "Home phone", "Mobile phone")
                )
                add_radio = st.radio(
                        "Choose a shipping method",
                        ("Standard (5-15 days)", "Express (2-5 days)")
                    )
            """
        )
        # Using object notation
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone")
        )
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )
def layouts():
    st.header("Layouts and Containers")
    with st.expander("Container"):
        st.subheader("Container")
        st.text("Insert a multi-element container.")
        with st.container():
            st.code(
                """
                with st.container():
                    st.write("This is inside the container")

                    # You can call any Streamlit command, including custom components:
                    st.bar_chart(np.random.randn(50, 3))

                st.write("This is outside the container")
                """
            )
            with st.container():
                st.write("This is inside the container")

                # You can call any Streamlit command, including custom components:
                st.bar_chart(np.random.randn(50, 3))

            st.write("This is outside the container")
    with st.expander("Columns"):
        st.subheader("Columns")
        st.text("We can have containers listed side by side")
        with st.container():
            st.text("Columns with same width just specify the number")
            st.code("""
            cols = st.columns(3)
            cols[0].text("this is col 1")
            cols[1].text("this is col 2")
            cols[2].text("this is col 3")
                                    """)
            cols = st.columns(3)
            cols[0].text("this is col 1")
            cols[1].text("this is col 2")
            cols[2].text("this is col 3")
        with st.container():
            st.text("Columns with variable with width")
            st.code("""
            col1, col2 = StructuralElements.columns([3, 1])
            col1.text("A wide column........................................")
            col2.text("A narrow column......................................")
                                    """)
            col1, col2 = st.columns([3, 1])
            col1.text("A wide column........................................")
            col2.text("A narrow column......................................")
    with st.expander("Popover"):
        st.subheader("Popover")
        with st.container():
            st.code("""
            with st.popover("Open popover"):
                st.markdown("Hello World 👋")
                name = st.text_input("What's your name?")
                st.write("Your name:", name)
                    """)
            with st.popover("simple popover"):
                    st.markdown("Hello World 👋")
                    name = st.text_input("What's your name?")
                    st.write("Your name:", name)
        with st.container():
            st.code(
                """
            popover = st.popover("Filter items")
            red = popover.checkbox("Show red items.", True)
            blue = popover.checkbox("Show blue items.", True)
            if red:
                st.write(":red[This is a red item.]")
            if blue:
                st.write(":blue[This is a blue item.]")
    """
            )
            popover = st.popover("Filter items")
            red = popover.checkbox("Show red items.", True)
            blue = popover.checkbox("Show blue items.", True)
            if red:
                st.write(":red[This is a red item.]")
            if blue:
                st.write(":blue[This is a blue item.]")
    with st.expander("Empty"):
        st.subheader("Empty")
        with st.container():
            st.text('Overwriting elements in-place using "with" notation:')
            st.code(
            """
            with st.empty():
                for seconds in range(60):
                    st.write(f"⏳ {seconds} seconds have passed")
                    time.sleep(1)
                st.write("✔️ 1 minute over!")
            """)
            with st.empty():
                for seconds in range(5):
                    st.write(f"⏳ {seconds} seconds have passed")
                    time.sleep(1)
                st.write("✔️ 5 seconds over!")
        with st.container():
            st.text("Replacing several elements, then clearing them:")
            st.code(
                """
                placeholder = st.empty()

                # Replace the placeholder with some text:
                placeholder.text("Hello")

                # Replace the text with a chart:
                placeholder.line_chart({"data": [1, 5, 2, 6]})

                # Replace the chart with several elements:
                with placeholder.container():
                    st.write("This is one element")
                    st.write("This is another")

                # Clear all those elements:
                placeholder.empty()
                """)
            placeholder = st.empty()

            # Replace the placeholder with some text:
            placeholder.text("Hello")

            # Replace the text with a chart:
            placeholder.line_chart({"data": [1, 5, 2, 6]})

            # Replace the chart with several elements:
            with placeholder.container():
                st.write("This is one element")
                st.write("This is another")

            # Clear all those elements:
            placeholder.empty()
    with st.expander("SideBar"):        
        st.text("check out the side and expand it")