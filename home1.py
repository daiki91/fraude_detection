import streamlit as st

# Charger le contenu du fichier CSS généré
def load_css(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Path to the CSS file
css_file_path = 'output.css'
css = load_css(css_file_path)

# Utiliser le CSS dans l'application Streamlit
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# HTML for the preloader
preloader_html = """
<div id="preloader">
    <div id="ctn-preloader" class="ctn-preloader items-center flex h-full justify-center fixed w-full z-[999999] left-0 top-0 bg-white">
        <div class="animation-preloader absolute z-[100] text-center">
            <div class="icon inline-block relative">
                <img src="images/logo/logo_01.svg" alt="" class="m-auto block animate-[rotated_12s_infinite_linear]" width="40">
            </div>
            <div class="txt-loading mt-3 select-none">
                <span data-text-preloader="e-" class="letters-loading font-bold tracking-[12px] inline-block text-[rgb(255_50_148_/_20%)] relative text-[35px] leading-[30px] font-Recoleta before:animate-[letters-loading_4s_infinite] before:text-[color:var(--prime-ten)] before:content-[attr(data-text-preloader)] before:opacity-0 before:leading-[30px] before:absolute before:left-0 before:top-0">
                    e-
                </span>
                <span data-text-preloader="L" class="letters-loading font-bold tracking-[12px] inline-block text-[rgb(255_50_148_/_20%)] relative text-[35px] leading-[30px] font-Recoleta before:animate-[letters-loading_4s_infinite] before:text-[color:var(--prime-ten)] before:content-[attr(data-text-preloader)] before:opacity-0 before:leading-[30px] before:absolute before:left-0 before:top-0">
                    L
                </span>
                <span data-text-preloader="AA" class="letters-loading font-bold tracking-[12px] inline-block text-[rgb(255_50_148_/_20%)] relative text-[35px] leading-[30px] font-Recoleta before:animate-[letters-loading_4s_infinite] before:text-[color:var(--prime-ten)] before:content-[attr(data-text-preloader)] before:opacity-0 before:leading-[30px] before:absolute before:left-0 before:top-0">
                    AA
                </span>
                <span data-text-preloader="BB" class="letters-loading font-bold tracking-[12px] inline-block text-[rgb(255_50_148_/_20%)] relative text-[35px] leading-[30px] font-Recoleta before:animate-[letters-loading_4s_infinite] before:text-[color:var(--prime-ten)] before:content-[attr(data-text-preloader)] before:opacity-0 before:leading-[30px] before:absolute before:left-0 before:top-0">
                    BB
                </span>
            </div>
        </div>    
    </div>
</div>
"""

# HTML for the hero banner
hero_banner_html = """
<div class="hero-banner-five text-center relative bg-cover z-[1] px-0 py-[300px] bg-[url(../images/assets/hero_01.png)] bg-no-repeat bg-[center_bottom] md:p-[200px_0] sm:p-[200px_0] xsm:p-[200px_0]">
    <div class="container">
        <div class="flex flex-wrap mx-[-12px]">
            <div class="xl:w-10/12 w-full flex-[0_0_auto] px-[12px] max-w-full m-auto wow fadeInUp" data-wow-delay="0.2s">
                <h1 class="hero-heading text-white mb-[50px] md:mb-[30px] sm:mb-[30px] xsm:mb-[30px] text-[170px] leading-[0.73em] tracking-[-2px] font-Eustache lg:text-[130px] md:text-[90px] md:leading-[0.9em] sm:text-[90px] sm:leading-[0.9em] xsm:text-[90px] xsm:leading-[0.9em]">
                    Get <span class="relative">Loud <img class=" absolute -translate-x-2/4 -translate-y-2/4 z-[-1] max-w-[initial] left-2/4 top-2/4 md:max-w-[150%] sm:max-w-[150%] xsm:max-w-[150%]" src="images/shape/shape_71.svg" alt=""></span> 
                    <br> Raise your Voice Today
                </h1>
            </div>
        </div>
        <a href="contact-us.html" class="donate-btn font-medium tran3s wow fadeInUp text-[17px] leading-[60px] text-black p-[0_48px] rounded-[30px] bg-[var(--prime-four)] hover:bg-white lg:text-[15px] lg:leading-[50px] lg:p-[0_40px] md:text-[15px] md:leading-[50px] md:p-[0_40px] sm:text-[15px] sm:leading-[50px] sm:p-[0_40px] xsm:text-[15px] xsm:leading-[50px] xsm:p-[0_40px]" data-wow-delay="0.4s">Donate now</a>
    </div>
</div>
"""

# Utiliser les HTML dans l'application Streamlit
st.markdown(preloader_html, unsafe_allow_html=True)
st.markdown(hero_banner_html, unsafe_allow_html=True)

# Votre contenu Streamlit ici
st.title("Mon home 1")
st.write("Voici un exemple d'application utilisant Tailwind CSS.")
