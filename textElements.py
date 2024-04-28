import streamlit as st

def textElements():
    st.header("HEADINGS & BODY")
    with st.expander("Title"):
        st.subheader("Title")
        with st.echo():
            st.title('This is a title')
            st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    with st.expander("Header"):
        st.subheader("Header")
        with st.echo():
            st.header('This is a header with a divider', divider='rainbow')
            st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    with st.expander("SubHeader"):
        st.subheader("SubHeader")
        with st.echo():
            st.subheader('This is a subheader with a divider', divider='rainbow')
            st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
    with st.expander("Markdown"):
        st.subheader("Markdown")
        with st.echo():
            st.markdown("*Streamlit* is **really** ***cool***.")
            st.markdown('''
                :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
                :gray[pretty] :rainbow[colors].''')
            st.markdown("Here's a bouquet &mdash;\
                        :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

            multi = '''If you end a line with two spaces,
            a soft return is used for the next line.

            Two (or more) newline characters in a row will result in a hard return.
            '''
            st.markdown(multi)
    st.header("FORMATTED TEXT")
    with st.expander("Caption"):
        st.subheader("Caption")
        with st.echo():
            st.caption('This is a string that explains something above.')
            st.caption('A caption with _italics_ :rainbow[colors] and emojis :sunglasses:')
    with st.expander("Code"):
        st.subheader("Code")
        with st.echo():
            code = '''def hello():
                print("Hello, Streamlit!")'''
            st.code(code, language='python')
    with st.expander("Divider"):
        st.subheader("Divider")
        with st.container():
            with st.echo():
                st.divider()
        # with st.echo:
        #     st.text("This is some text.")
        #     st.slider("This is a slider"s, 0, 100, (25, 75))
        #     st.divider()  # 👈 Draws a horizontal rule
        #     st.text("This text is between the horizontal rules.")
        #     st.divider()  # 👈 Another horizontal rule
    with st.expander("Echo"):
        st.subheader("Echo")
        st.text("Use in a with block to draw some code on the app, then execute it.")
        with st.echo():
            def get_user_name():
                return 'John'
            with st.echo():
                # Everything inside this block will be both printed to the screen
                # and executed.

                def get_punctuation():
                    return '!!!'

                greeting = "Hi there, "
                value = get_user_name()
                punctuation = get_punctuation()

                st.write(greeting, value, punctuation)

            # And now we're back to _not_ printing to the screen
            foo = 'bar'
            st.write('Done!')
    with st.expander("Latex-Equations"):
        st.subheader("Latex")
        with st.echo():
            st.latex(r'''
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
                ''')
    with st.expander("Text"):
        st.subheader("Text")
        with st.echo():
            st.text('This is some text.')