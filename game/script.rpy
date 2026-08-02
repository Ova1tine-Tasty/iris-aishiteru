# character
define s = Character("ชิน", color="#000000")
define n = Character("นัท", color="#000000")
define k = Character("เก่ง", color="#000000")
define uk = Character("???", color="#000000")
define npc1 = Character("รปภ", color="#000000")

# phone
define s_nvl = Character("shin", kind=nvl, callback=Phone_SendSound)
define k_nvl = Character("Kenglnwza007", kind=nvl, callback=Phone_ReceiveSound)
define n_nvl = Character("Kurumi<3", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# bg
image white = "#ffffff"
image bg Livingroom_Day = "backgrounds/Livingroom_Day.png"
image bg Apartment_Exterior = "backgrounds/Apartment_Exterior.png"
image bg Train_Day = "backgrounds/Train_Day.png"
image bg Train_Night = "backgrounds/Train_Night.png"
image bg BusStop_Spring_Day = "backgrounds/BusStop_Spring_Day.png"
image bg BusStop_Spring_Night = "backgrounds/BusStop_Spring_Night.png"
image bg BusStop_Spring_Afternoon = "backgrounds/BusStop_Spring_Afternoon.png"
image bg City_Morning = "backgrounds/City_Morning.png"
image bg City_Afternoon = "backgrounds/City_Afternoon.png"
image bg City_Night = "backgrounds/City_Night.png"
image bg Restaurant_B = "backgrounds/Restaurant_B.png"
image bg Outdoor_Stairs = "backgrounds/Outdoor_Stairs.png"
image bg Classroom_Day = "backgrounds/Classroom_Day.png"
image bg Old_School = "backgrounds/Old_School.png"
image bg School_Hallway_Day = "backgrounds/School_Hallway_Day.png"
image bg Backstreet_Spring_Afternoon = "backgrounds/Backstreet_Spring_Afternoon.png"
image bg Street_Spring_Evening = "backgrounds/Street_Spring_Evening.png"
image bg Shrine_Spring_Day = "backgrounds/Shrine_Spring_Day.png"
image bg Old_FestivalB = "backgrounds/Old_FestivalB.png"
image bg Old_FestivalC = "backgrounds/Old_FestivalC.png"
image bg Train_Evening = "backgrounds/Train_Evening.png"
image bg Cafeteria_Day = "backgrounds/Cafeteria_Day.png"
image bg Old_FuneralNut = "backgrounds/Old_FuneralNut.png"
image bg BusStop_Summer_Afternoon = "backgrounds/BusStop_Summer_Afternoon.png"
image bg Bedroom_Day = "backgrounds/Bedroom_Day.png"
image bg Street_Summer_Evening = "backgrounds/Street_Summer_Evening.png"
image bg Livingroom_Night = "backgrounds/Livingroom_Night.png"
image bg Backstreet_Summer_Afternoon = "backgrounds/Backstreet_Summer_Afternoon.png"
image bg Temple_Spring_Day = "backgrounds/Temple_Spring_Day.png"
image bg Street_Summer_Stars = "backgrounds/Street_Summer_Stars.png"

# char
# Nut uni
image nut uni smile:
    "characters/Nut/Aiko_Blazer_Smile.png"
    zoom 0.22
image nut uni smile b:
    "characters/Nut/Aiko_B_Blazer_Smile.png"
    zoom 0.22
image nut uni smile blush:
    "characters/Nut/Aiko_Blazer_Smile_Blush.png"
    zoom 0.22
image nut uni frown:
    "characters/Nut/Aiko_Blazer_Frown.png"
    zoom 0.22
image nut uni frown b:
    "characters/Nut/Aiko_B_Blazer_Frown.png"
    zoom 0.22
image nut uni open:
    "characters/Nut/Aiko_Blazer_Open.png"
    zoom 0.22
image nut uni open b:
    "characters/Nut/Aiko_B_Blazer_Open.png"
    zoom 0.22
image nut uni closed open:
    "characters/Nut/Aiko_Blazer_Closed_Open.png"
    zoom 0.22
image nut uni closed open b:
    "characters/Nut/Aiko_B_Blazer_Closed_Open.png"
    zoom 0.22
image nut uni closed open blush:
    "characters/Nut/Aiko_Blazer_Closed_Open_Blush.png"
    zoom 0.22
image nut uni closed open blush b:
    "characters/Nut/Aiko_B_Blazer_Closed_Open_Blush.png"
    zoom 0.22
image nut uni closed open angry:
    "characters/Nut/Aiko_Blazer_Closed_Open_Angry.png"
    zoom 0.22
image nut uni closed smile:
    "characters/Nut/Aiko_Blazer_Closed_Smile.png"
    zoom 0.22
image nut uni closed smile b:
    "characters/Nut/Aiko_B_Blazer_Closed_Smile.png"
    zoom 0.22
image nut uni closed frown:
    "characters/Nut/Aiko_Blazer_Closed_Frown.png"
    zoom 0.22
image nut uni closed frown b:
    "characters/Nut/Aiko_B_Blazer_Closed_Frown.png"
    zoom 0.22
image nut uni closed smile blush:
    "characters/Nut/Aiko_Blazer_Closed_Smile_Blush.png"
    zoom 0.22
# Nut casual
image nut casual smile:
    "characters/Nut/Aiko_Casual_Smile.png"
    zoom 0.22
image nut casual smile blush:
    "characters/Nut/Aiko_Casual_Smile_Blush.png"
    zoom 0.22
image nut casual frown blush:
    "characters/Nut/Aiko_Casual_Frown_Blush.png"
    zoom 0.22
image nut casual frown:
    "characters/Nut/Aiko_Casual_Frown.png"
    zoom 0.22
image nut casual open:
    "characters/Nut/Aiko_Casual_Open.png"
    zoom 0.22
image nut casual closed open:
    "characters/Nut/Aiko_Casual_Closed_Open.png"
    zoom 0.22
image nut casual closed open blush:
    "characters/Nut/Aiko_Casual_Closed_Open_Blush.png"
    zoom 0.22
image nut casual closed smile:
    "characters/Nut/Aiko_Casual_Closed_Smile.png"
    zoom 0.22
image nut casual closed frown:
    "characters/Nut/Aiko_Casual_Closed_Frown.png"
    zoom 0.22
image nut casual closed smile blush:
    "characters/Nut/Aiko_Casual_Closed_Smile_Blush.png"
    zoom 0.22

image nut casual closed open angry:
    "characters/Nut/Aiko_Casual_Closed_Open_Angry.png"
    zoom 0.22

# Keng
image keng casual open:
    "characters/Keng/Sora_Casual_Open.png"
    zoom 0.67
image keng casual smile:
    "characters/Keng/Sora_Casual_Smile.png"
    zoom 0.67
image keng casual frown:
    "characters/Keng/Sora_Casual_Frown.png"
    zoom 0.67
image keng uni smile:
    "characters/Keng/Sora_WinterUni_Smile.png"
    zoom 0.67
image keng uni frown:
    "characters/Keng/Sora_WinterUni_Frown.png"
    zoom 0.67
image keng uni open:
    "characters/Keng/Sora_WinterUni_Open.png"
    zoom 0.67

label start:
    $ quick_menu = False
    stop music fadeout 1.0
    scene black
    pause 3.0
    
    centered "{color=#ffffff}{w=1}ในช่วงชีวิตของคนๆหนึ่งมีเวลาอยู่ราว 80 ปี\n{w=1.5}หากเปรียบช่วงเวลาเหล่านั้นเป็นม้วนฟิล์มก็จะมีความยาวประมาณ 1.15 ล้านกิโลเมตร{/color}"
    centered "{color=#ffffff}บางส่วนของม้วนฟิล์มนั้นอาจบิดเบี้ยว เสียหาย หรือเลือนลางจนไม่สามารถกรอกลับมาดูได้ใหม่{/color}"
    centered "{color=#ffffff}แต่ก็ยังคงเหลือร่องรอยที่บอกว่าครั้งหนึ่งเรื่องราวเหล่านั้นเคยเกิดขึ้นจริง{/color}"
    centered "{color=#ffffff}หากความทรงจำเป็นเหมือนม้วนฟิล์มที่สามารถกรอกลับมาดูได้ใหม่ คุณจะเลือกย้อนกลับไปยังส่วนไหนของเรื่องราว?{/color}"

    pause 1.5

    s "มีคนเคยบอกผมว่าชีวิตก็เหมือนกับหนัง\nและความทรงจำก็เปรียบดั่งม้วนฟิล์มที่บันทึกเรื่องราวต่างๆเอาไว้"
    s "หนังที่มีตัวเราเป็นผู้กำกับและประพันธ์เรื่องราวต่างๆด้วยตัวเอง"
    s "แต่สำหรับผมมีอีกหนึ่งคนที่คอยเติมสีสันให้เรื่องราวของผมมีชีวิตชีวามากกว่าเก่า เมื่อไหร่ก็ตามที่มองย้อนกลับไปผมก็จะคิดถึงคนๆนั้นเสมอ"
    s "เธอผู้เปรียบดั่งสีสันในช่วงเวลามัธยมปลายของผม แม้เวลาจะผ่านล่วงเลยมาหลายปี\nนับตั้งแต่จบการศึกษาแต่ภาพของเธอก็ยังคงไม่ลบเลือนหายไป"
    
    play music "audio/Sketchbook 2024-09-25.ogg" fadein 1.5 fadeout 1.5
    scene bg Livingroom_Day with fade
    $ quick_menu = True
    s "(เช้าตรู่ของวันจันทร์ ผมรีบจัดแจงเสื้อผ้าหน้าผมและสะพายกระเป๋าโน๊ตบุ๊ค\nอันแสนสำคัญเพื่อเตรียมไปทำงาน)"
    scene bg BusStop_Spring_Day
    s "(การเดินทางก็ไม่ได้สะดวกมากนักผมต้องนั่งรถเมล์หนึ่งต่อ\nเพื่อไปขึ้นรถไฟฟ้าอีกหนึ่งเที่ยวจากนั้นจึงจะถึงที่ทำงาน)"
    s "(ทำไงได้ล่ะก็ค่าเช่าคอนโดแถวนั้นก็ไม่ใช่ถูกๆเลย)"
    s "?"
    s "วันนี้มาเช้าจังเลยนะ"
    show keng casual smile with dissolve
    k "ก็นะ วันนี้วันจันทร์ขืนไปสายเดี๋ยวได้โดนตัดเงินเดือนกันพอดี"
    scene bg Train_Day with fade
    show keng casual smile with dissolve
    s "(คนตรงหน้านี้คือเก่ง ผมกับเก่งรู้จักกันมานานแล้ว เราเรียนมัธยมด้วยกันพอจบมาก็ต่างคนต่างไปเรียนสาขาที่อยากเรียน แต่ด้วยความบังเอิญหรือเหตุผลบางอย่างผมกับเขาก็มาลงเอยในที่ทำงานเดียวกัน)"
    scene bg City_Morning with fade
    show keng casual open with dissolve
    k "มาเช้าขนาดนี้กินข้าวก็ทันนะ"
    s "ไม่อะ กาแฟสักแก้วรองท้องก็พอแล้ว"
    show keng casual frown
    k "กินแต่กาแฟเดี๋ยวก็เป็นกรดไหลย้อนพอดี"
    k "แล้วแต่นายละกันฉันจะไปหาอะไรกินสักหน่อย แล้วเจอกันบนตึกนะ"
    s "อือ แล้วเจอกัน"

    scene black with fade
    play sound "audio/Keyboard Typing Sound Effect Fast.mp3"
    centered "{color=#ffffff}{size=+40}12:00{/size}{/color}"
    stop sound
    scene bg Outdoor_Stairs with fade
    pause 3.0
    scene bg City_Morning with dissolve
    s "?"
    show keng casual smile with dissolve
    s "มีอะไรหรอ"
    k "เที่ยงแล้วเพื่อน ไปกินข้าวได้แล้ว"
    menu keng_lunch:
        k "{cps=0}เที่ยงแล้วเพื่อน ไปกินข้าวได้แล้ว{/cps}"
        "ไปกินข้าวกับเก่ง":
            s "โอเค ฉันซื้อกาแฟแปปนึง"
            k "งั้นไปกินร้านเดิมนะ เดี๋ยวฉันรอ"
        "ปฏิเสธและนั่งทำงานต่อ":
            s "นายไปกินก่อนเลย ฉันว่าจะซื้อแค่กาแฟแล้วก็กลับไปทำงานต่อ"
            show keng casual frown
            k "..."
            show keng casual open
            k "มากินเถอะน่า ไม่งั้นฉันจะตามตื้อนายไปเรื่อยๆนี่แหละ"
            s "อ่าๆๆ ไปก็ได้"
            show keng casual smile
            s "ให้ตายสิ"

    scene bg Restaurant_B with fade
    show keng casual open with dissolve
    k "ชิน นายเนี่ยโหมงานไปหน่อยรึเปล่า นี่มันพึ่งจะวันจันทร์เองนะ\nทำซะเหมือนจะส่งวันนี้พรุ่งนี้"
    show keng casual frown
    s "ฉันรีบทำให้เสร็จจะได้พักนานๆไง นี่บ่นแต่ฉันของนายล่ะเริ่มบ้างรึยัง"
    show keng casual open
    k "คิดว่าฉันนั่งเฉยๆกินแรงชาวบ้านเขาไปวันๆรึไง ฉันทำเสร็จไปหลายอย่างแล้วเหมือนกันนั่นแหละ"
    show keng casual frown
    s "(เก่งกับผมมักจะมากินข้าวกลางวันที่นี่ด้วยกัน หนึ่งก็เพราะมันอยู่ค่อนข้างใกล้ที่ทำงานแถมรสชาติก็ไม่ได้แย่)"
    scene black with fade
    s "(ผมกับเก่งนั่งคุยกันอยู่สักพักก่อนจะกลับไปทำงาน เวลาจากนี้ผมจะนั่งแก้บัคส่วนที่ยังค้างคาให้เสร็จแล้วก็เขียนส่วนอื่นต่อเลย)"

    play sound "audio/Keyboard Typing Sound Effect Fast.mp3"
    centered "{w=3}{color=#ffffff}{size=+40}18:30{/size}{/color}"
    stop sound
    s "6 โมงครึ่งแล้วหรอเนี่ย"
    s "ลืมเวลาไปซะสนิทเลย"
    
    scene bg City_Night
    with fade
    npc1 "กลับเย็นอีกแล้วหรอครับวันนี้"
    s "ครับผม พอดีงานพึ่งเสร็จน่ะครับ"
    npc1 "ขยันทำงานก็ดีแต่ก็อย่าลืมดูแลสุขภาพด้วยนะครับ ผมเห็นคุณชินกลับบ้านดึกวันเลย"
    s "ขอบคุณที่เป็นห่วงนะครับลุง ลุงก็เช่นกันครับ"
    s "(ลุงแดงเป็นรปภ.ที่นี่มาก่อนที่ผมจะมาทำงานเสียอีก อายุน่าจะปาไปหกสิบแล้ว\nแต่ยังเดินปร๋ออยู่เลย)"
    scene bg Train_Night with fade
    s "(เช่นเคยผมต้องนั่งรถไฟฟ้าหนึ่งเที่ยวก่อนจะต่อรถเมล์เพื่อกลับคอนโด)"
    s "(ชีวิตก็เป็นแบบนี้วนไปทุกวันๆผมไม่ได้รู้สึกเบื่อในขณะเดียวกัน\nก็ไม่ได้รู้สึกมีความสุขขนาดนั้น)"
    s "(ถ้าผมเอาเรื่องนี้ไปบ่นให้เธอฟังเธอจะพูดว่ายังไงกันนะ)"
    s "('นายน่ะหัดใช้ชีวิตให้มันมีสีสันบ้างสิ' ไม่ก็)"
    s "('ชีวิตแบบนั้นฉันได้เฉาตายแน่' แล้วก็คงทำหน้าเซ็งๆใส่ล่ะมั้ง)"
    s "(จะว่าไปก็น่าคิดถึงจังเลยนะช่วงเวลาสมัยนั้น)"
    $ quick_menu = False
    scene black with fade
    s "(อ้อใช่ผมลืมบอกไปนอกจากเก่งที่เป็นเพื่อนสนิทสมัยมัธยมปลายแล้วก็ยังมีอีกคนนึง)"
    s "(จะบอกว่าสนิทกว่าเก่งไหมก็ไม่เชิงแต่ด้วยเหตุผลบางอย่างเธอมักจะ\nติดสอยห้อยตามผมไปตลอด ส่วนตัวผมก็ไม่ได้ไม่ชอบหรือเกลียดอะไร\nเพราะอย่างน้อยก็มีเพื่อนไว้คุยเล่นบ้าง)"
    s "(เธอชื่อนัท สมัยม.ปลายถ้าผมไม่ไปกับเก่งนัทก็คือคนที่จะมาติดตามผมไปด้วย หรือบางทีผมไปกับเก่งสองคนเธอก็จะมาตามติดพวกผมอยู่ดี)"
    s "(เพื่อนๆทุกคนรักนัท ส่วนหนึ่งก็เพราะความเฟรนลี่ของเธอที่เข้ากับคนอื่นได้ง่าย แถมยังเป็นเด็กกิจกรรมที่คอยช่วยเหลือเพื่อนๆตลอดเวลา)"
    s "(อีกส่วนหนึ่งคือนิสัยชอบทำอะไรบ้าๆบอๆของเธอซึ่งก็ดีบ้างไม่ดีบ้าง แต่โดยรวมก็นับว่าเป็นอีกหนึ่งดาวเด่นของห้องเลยทีเดียว)"
    s "(ตอนเลิกเรียนเธอมักจะมาบ่นนั่นบ่นนี่ให้ผมฟังประจำแต่ผมก็ชอบฟังนะ เวลาเธอพูดเธอมักจะออกท่าออกทางบางทีก็รู้สึกเหมือนดูละครอยู่เหมือนกัน)"
    s "(สำหรับผมนัทเป็นคนที่แต่งเติมสีสันให้เรื่องราวต่างๆของผมมีชีวิตชีวามากกว่าเก่า เป็นคนที่ทำให้ชีวิตม.ปลายของผมกลายเป็นไฮไลท์สำคัญที่น่าจดจำมาจนถึงทุกวันนี้)"
    window hide

    play sound "audio/Old Movie The End Film With Sound Effect HD FREE.mp3"
    pause 7.0
    stop sound

    jump in_to_the_memory


label in_to_the_memory:
    scene bg Old_School with fade
    play music "audio/Ludum Dare 38 01.ogg" fadein 0.5
    $ quick_menu = True
    s "(วันนี้เป็นวันเปิดภาคเรียนม.ปลายเทอมแรกของผม บอกตามตรงว่าบรรยากาศ\nก็ไม่ได้ต่างไปจากตอนที่ผมอยู่ม.ต้นมากสักเท่าไหร่ บรรยากาศเดิมๆ\nกับตึกหน้าตาเหมือนเดิม)"
    scene bg Classroom_Day with dissolve
    show keng uni smile with moveinleft
    k "โย่ว! ชิน"
    s "เห้ย! อยู่ห้องเดียวกันด้วยหรอโชคดีชะมัด"
    s "(ผมกับเก่งเคยอยู่ห้องเดียวกันตอนม.ต้น เราสนิทกันมากเพราะชอบอะไรเหมือนๆกัน พอม.ปลายก็บังเอิญได้อยู่ห้องเดียวกันอีกถ้าบอกว่าโชคช่วยก็คงไม่ผิดอะไรนัก)"
    hide keng uni smile with dissolve
    s "(เพื่อนๆในห้องเริ่มทำความรู้จักกัน บ้างก็ถามว่าตอนม.ต้นอยู่ห้องอะไร\nหรือมาจากโรงเรียนอะไร)"
    s "(ส่วนพวกผมสองคนก็ไม่ค่อยมีใครมาคุยด้วยเท่าไหร่เพราะสมาชิกในห้องส่วนใหญ่\nรู้จักพวกผมกันดีอยู่แล้ว ก็มาจากห้องเดียวกันตอนม.ต้นนี่นะ)"
    show nut uni smile b with dissolve
    s "?"
    show nut uni open b
    uk "นี่ นายชื่ออะไรหรอ"
    show nut uni smile b
    s "อ่า...เราชื่อชินน่ะ แล้วเธอล่ะ"
    show nut uni closed open b with dissolve
    n "เราชื่อนัทนะพึ่งย้ายมาใหม่ ยินดีที่ได้รู้จักนะชิน!"
    show nut uni smile b with dissolve
    s "อื้ม ยินดีที่ได้รู้จักเช่นกันนะนัท"
    hide nut uni smile b with dissolve
    s "(แล้วเธอก็เดินไปทักทายคนอื่นๆในห้องด้วยใบหน้าที่ยิ้มแย้มต่อ)"
    show keng uni smile
    with vpunch
    k "โอ๊ะ ไม่เบานี่หว่า"
    s "อะไรๆ คิดจะแซวกันรึไง"
    k "คนนั้นเนี่ยก็หน้าตาดีไม่เบาเลยนะ"
    menu keng_tease:
        k "{cps=0}คนนั้นเนี่ยก็หน้าตาดีไม่เบาเลยนะ{/cps}"
        "เห็นด้วย":
            s "อืม{w=1}.{w=1}.{w=1}.ก็น่ารักจริงๆนั่นแหละ"
            k "ใช่มั้ยล่ะ"
            show keng uni open
            k "แต่คู่แข่งน่าจะเยอะนะเนี่ย คงจะฮ็อตน่าดู"
            show keng uni smile
            k "รีบทำแต้มตั้งแต่คู่แข่งน้อยๆดีกว่านะ~"
            s "ก็แย่ละ เห็นฉันเป็นอาหวังรึไง ฉันแค่ชมตามความรู้สึกกับสิ่งที่เห็นเท่านั้นแหละ ไม่ได้จะทำแต้มซะหน่อย"
            k "คร้าบ คร้าบ พ่อเทพบุตร"
        "แซวกลับ":
            s "นายคิดจะจีบนักเรียนใหม่ตั้งแต่วันแรกที่เจอเลยรึไง"
            k "เปล่าสักหน่อย แค่ชมว่าคนที่มาทักนายน่ะหน้าตาดีเท่านั้นเอง\nอย่าพึ่งมองฉันผิดไปเลยเพื่อนเอ๋ย"
            s "(ก็จริงอย่างที่เขาว่า ผมสนิทกับเก่งมากพอจะรู้ว่าอันไหนพูดจริงอันไหนพูดเล่น)"
            s "แต่ก็น่ารักจริงอย่างที่นายว่านั่นแหละ"

    scene bg BusStop_Spring_Afternoon with fade
    show keng uni open with dissolve
    k "เห้อ...เรียนวันแรกก็ล้าไปหมดทั้งตัวแล้ว ตอนม.ต้นไม่เห็นเลิกเย็นแบบนี้เลย"
    show keng uni frown
    s "ตอนม.ต้นเราเรียนเยอะขนาดนี้ที่ไหนล่ะ เรียนไปเรื่อยๆเดี๋ยวก็ชินเองแหละน่า"
    show keng uni open
    k "นั่นสินะ"

    jump nickname

label nickname:
    scene black with fade
    centered "{color=#ffffff}{size=+20}หลายเดือนผ่านไป{/size}{/color}"
    scene bg Classroom_Day with fade
    play music "audio/Ludum Dare 38 01.ogg" fadein 0.5
    show nut uni closed open with dissolve
    n "สมาร์ท~"
    hide nut uni closed open with dissolve
    show keng uni open with dissolve
    k "นี่ชิน ห้องเรามีคนชื่อสมาร์ทด้วยหรอ"
    show keng uni frown
    s "ไม่มีนะ"
    show keng uni frown with move:
        xalign 0.3
        yalign 1.0
    show nut uni open with dissolve:
        xalign 0.7
        yalign 1.0
    n "ฉันเรียกนายต่างหากเก่ง"
    show nut uni smile
    show keng uni open
    k "ห๋า? อะไรของเธอเนี่ยฉันชื่อเก่งไม่ได้ชื่อสมาร์ท"
    show nut uni open
    show keng uni frown
    n "ก็สมาร์ทแปลว่าเก่งไง"
    show nut uni smile
    show keng uni open
    k "เห้อ"
    k "มุก 5 บาท 10 บาทก็เล่น"
    show nut uni open
    show keng uni frown
    n "เท่ดีออก สมาร์ท"
    show nut uni smile
    show keng uni open
    k "ชื่อโหลเป็นบ้า"
    show nut uni open
    show keng uni frown
    n "ส่วนชินก็..."
    show nut uni smile
    s "ฉันด้วยอ่อ?"
    show nut uni closed open
    n "ชื่อใหม่ละกัน"
    show nut uni smile
    s "ห๊ะ?"
    show nut uni open
    n "ภาษาญี่ปุ่นไง"
    show nut uni smile
    s "เอาที่เธอสบายใจเลย"
    show keng uni open
    k "ส่วนเธอชื่อถั่วเขียวดีมั้ย"
    show keng uni smile
    show nut uni frown with vpunch
    n "ไม่เอาอะ โบราณเกิน"
    k "นัทโต๊ะ"
    n "ไม่เอา"
    show nut uni smile
    with vpunch
    k "ทีพวกฉันยังปฏิเสธไม่ได้เลยเห้ย"
    show keng uni frown
    show nut uni frown
    s "คุรุมิมั้ย"
    show keng uni smile
    k "ฟังดูเข้าท่าแหะ"
    s "คุรุมิแปลว่าวอลนัต ก็ดูเข้ากับชื่อเธอดี"
    show nut uni open
    n "งั้นเอาชื่อนี้ละกัน คุรุมิ"
    show nut uni closed open
    n "ชื่อน่ารักดี"

    jump movie
    
    
label movie:
    scene black with fade
    pause 3.0
    scene bg School_Hallway_Day with fade

    window hide
    nvl clear
    play audio "audio/iPhone Notification Vibrate Sound Effect.mp3"
    "{i}ครืดๆ{/i}"
    s "?"
    s "(ใครทักมานะ)"
    k_nvl "เสาร์นี้ว่างมั้ย จะชวนไปเดินเล่นห้าง"
    s_nvl "ไม่อะ ขี้เกียดไป"
    s_nvl "ฉันจะฟาร์มเพชรไว้กด\nกาชาตู้หน้า"
    k_nvl "จะรีบฟาร์มไปเปิดไวฟุว่างั้น"
    s_nvl "{image=emoji/thumb-up.png}"
    k_nvl "เคๆ ตามใจนายละกัน{image=emoji/wave.png}"
    nvl_narrator ""
    s "(วันหยุดแบบนี้ใครเขาจะปล่อยให้เสียเปล่ากัน)"
    n "ชินนนน!"
    s "(?)"
    show nut uni closed open with easeinright
    pause 0.2
    show nut uni open
    n "หวัดดีจ้า"
    show nut uni smile
    s "หวัดดีนัท"
    show nut uni open
    n "นี่ ฉันมีคำถามมาถามด้วยล่ะ"
    show nut uni smile
    s "ไม่เอาไก่กับไข่อะไรเกิดก่อนกันนะ อันนั้นมันเชยแล้ว"
    show nut uni closed open
    n "ไม่ใช่หรอกน่า รอบนี้ไม่มีมุกแน่นอน"
    show nut uni closed smile
    s "อาๆ ว่ามา"
    show nut uni open
    n "ชินชอบดูหนังรึเปล่า"
    menu do_you_like_movie:
        n "{cps=0}ชินชอบดูหนังรึเปล่า{/cps}"
        "ชอบดู":
            show nut uni open b with dissolve
            n "ชอบดูหนังแนวไหนหรอ"
            show nut uni smile b
            s "ก็พวกหนังแอ็กชัน หนังสืบสวน และก็อนิเมะน่ะ"
            s "แต่ฉันไม่ค่อยชอบดูหนังตามกระแสเท่าไหร่"
            
        "ไม่ค่อยได้ดู":
            show nut uni smile
            s "ไม่ค่อยได้ดูนะ นานๆดูที"
            s "ฉันไม่ค่อยชอบดูหนังตามกระแสเท่าไหร่"
            
    show nut uni open with dissolve
    n "งั้นหรอ{w=1.0}.{w=1.0}.{w=1.0}."
    show nut uni closed open with dissolve
    n "ว่าจะชวนไปดูหนังซะหน่อย {w=1.0}โดนตัดบทเลยนะเนี่ย"
    show nut uni smile with dissolve
    s "..."
    show nut uni frown
    s "งั้นเราก็ไปดูหนังด้วยกันมั้ยล่ะ"
    n "ไม่ใช่ว่านายบอกว่าไม่ชอบดูหนังตามกระแสหรอ"
    s "ก็นะ ฉันอยากรู้ว่าช่วงนี้คนเขาดูอะไรกันจะได้ไม่ตกเทรนด์ อีกอย่างหมอนั่นก็ชวนฉันไปเที่ยวด้วยไปกันหลายคนน่าสนุกจะตายไป"
    n "..."
    show nut uni closed smile with dissolve
    n "อื้อ ไปสิ"
    show nut uni smile with dissolve
    n "ไปกันหลายคนสนุกดีออก"
    scene black with dissolve
    pause 1.0
    $ nvl_show(dissolve)
    nvl_narrator "16:37{nw}"
    s_nvl "เก่ง"
    k_nvl "ว่าไงฮาฟฟู่"
    s_nvl "bruh"
    s_nvl "ฉันเปลี่ยนใจละ\nเจอกันวันเสาร์"
    k_nvl "????"
    k_nvl "ไหนบอกไม่ไป"
    s_nvl "พอดีมีหนังอยากดูน่ะ"
    s_nvl "ไหนๆก็ไปดูหนังแล้ว จะได้ไปเที่ยวด้วยกันเลย"
    k_nvl "ยอมทิ้งไวฟุเพื่อเพื่อนเลยหรอ\nเนี่ย ซึ้งจนน้ำตาไหลเลยT^T"
    s_nvl "..."
    s_nvl "แล้วก็"
    s_nvl "มีคนไปด้วยอีกคนนึงนะ"
    s "(ตู้หน้าฟาร์มช้าไปวันเดียวไม่เป็นไรหรอกมั้ง)"
    window hide

    centered "{color=#ffffff}{size=+20}วันเสาร์{/size}{/color}"
    scene bg Restaurant_B with fade

    nvl clear
    play audio "audio/iPhone Notification Vibrate Sound Effect.mp3"
    "{i}ครืดๆ{/i}"
    n_nvl "เอ่ออ"
    n_nvl "อันนี้ใช่แอคชินมั้ย"
    s_nvl "ใช่แล้ว อันนี้ใครหรอ"
    n_nvl "เรานัทเอง"
    n_nvl "คือฉันลืมว่าร้านที่นัดรวมกัน\nชื่ออะไร{image=emoji/sweat.png}"
    s_nvl "Iris Cafe"
    s_nvl "งั้นเดี๋ยวเราออกไปรอ\nที่หน้าร้านนะ"
    n_nvl "oki~ doki~"
    s "(จะว่าไป ไม่เห็นเก่งเลยแหะ)"
    s "(ตื่นสายแล้วล่ะมั้งเนี่ยหมอนั่น)"
    scene bg City_Morning with dissolve
    n "ชินน!"
    s "?"
    show nut casual closed smile with Dissolve(1.0)
    s "!"
    show nut casual open
    n "เดินหลงอยู่ตั้งนานแหนะ ดีนะที่นายออกมารับ"
    show nut casual smile
    s "อะ อืม"
    s "เดี๋ยวเราเข้าไปรอเก่งข้างในร้านก่อนดีกว่า จะได้ไม่ร้อนด้วย"
    show nut casual closed open
    n "โอ๊ะเค~"
    scene bg Restaurant_B with fade
    show keng casual smile with dissolve
    k "โย่วชิ..."
    show keng casual open
    k "ชิน.{w=0.5}.{w=0.5}.{w=0.5}ถ้าจะมาเดทก็บอกกันตรงๆก็ได้นะฉันไม่ว่าอะไรหรอก"
    show keng casual smile
    with vpunch
    s "ไม่ใช่เฟ้ย!"
    s "{cps=30}นัทชวนฉันมาดูหนังที่เดียวกับที่นายชวนฉันมาพอดีก็เลยคิดว่าไหนๆก็มาแล้ว\nจะได้ไปเที่ยวด้วยกันสามคนเลยก็น่าจะสนุกดี{/cps}{p}น่ะ"
    show keng casual smile with move:
        xalign 0.3
        yalign 1.0
    show nut casual closed open with dissolve:
        xalign 0.7
        yalign 1.0
    n "ทั้งสองคนอย่าพึ่งทะเลาะกันเลยนะ"
    show nut casual open
    n "ฉันเป็นคนขอให้ชินมาเป็นเพื่อนเองแหละ"
    show nut casual smile
    k "..."
    k "พวกนายนี่น้า..."
    s "นายก็มาดูหนังด้วยกันสิเก่ง"
    show keng casual open
    k "ไม่เอาอะ ไม่อยากเป็นก้างขวางคอ"
    show keng casual smile
    with vpunch
    s "ก็บอกว่าไม่ได้มาเดทไงเฟ้ย"
    show nut casual open
    n "มาเถอะน่าเก่ง นานๆทีจะได้มาเที่ยวด้วยกันครบแก๊งแบบนี้นะ"
    show nut casual smile
    show keng casual open
    k "เห้อ"
    show keng casual smile
    k "ไปก็ได้"
    show nut casual closed open
    n "เย่~"

    scene black with Fade(0.5, 3.0, 0.5)
    scene bg City_Morning with dissolve
    show keng casual open with dissolve:
        xalign 0.3
        yalign 1.0
    show nut casual smile with dissolve:
        xalign 0.7
        yalign 1.0
    k "ผิดคาดนะเนี่ย นึกว่าเธอจะชวนมาดูหนังสยองขวัญซะอีก"
    show nut casual frown
    show keng casual frown
    n "ฉันเห็นตัวอย่างหนังเรื่องนี้ในเน็ตน่ะ จริงๆก็เตรียมใจไว้แล้วล่ะ\nแต่ไม่นึกว่าจะปวดตับขนาดนี้"
    show keng casual open
    show nut casual smile
    k "ฉันว่าเขาเล่าเรื่องดีอยู่นะแต่มาหักมุมตอนท้ายนี่สิ ไม่ทันตั้งตัวเลย"
    k "นายว่าไงบ้างล่ะ"
    show keng casual frown
    s "ฉันหรอ?"
    s "ฉันว่าเป็นหนังอนิเมชั่นที่ดีเรื่องนึงเลยนะ เนื้อเรื่องดี เพลงดี ภาพก็สวย"
    s "แต่พอหักมุมตอนท้ายนี่ตั้งตัวไม่ทันจริงๆ น้ำตาซึมเลย"
    s "คงจะยกเป็นหนึ่งในเรื่องขึ้นหิ้งสำหรับฉันเลยล่ะ"
    
    scene bg City_Afternoon with Fade(0.5, 1.0, 0.5)

    show keng casual smile with dissolve
    k "ฉันกลับก่อนล่ะ พอดีที่บ้านมารับน่ะ"
    s "งั้นไว้เจอกันที่โรงเรียนนะ"
    k "พวกนายก็กลับบ้านกันดีๆด้วยล่ะ ไว้เจอกัน"
    
    play music "audio/Ludum Dare 32 02.ogg" fadein 1.5 fadeout 1.5
    scene bg Backstreet_Summer_Afternoon with Fade(0.5, 1.0, 0.5)
    pause 1.0
    show nut casual open with dissolve
    n "บางทีชีวิตเรานี่ก็เหมือนหนังเรื่องนึงเลยนะ นายว่ามั้ย"
    show nut casual smile
    s "อะไรของเธอเนี่ย จู่ๆก็พูดจามีวาทะศิลป์"
    show nut casual open
    n "ลองคิดดูนะ ถ้าเราเปรียบชีวิตเป็นเหมือนหนังและความทรงคือม้วนฟิล์ม\nเราจะย้อนกลับมาดูเมื่อไหร่ก็ได้ แต่พอเวลาผ่านไปนานมากขึ้นเรื่อยๆฟิล์มพวกนั้น\nก็จะค่อยๆเสื่อมสภาพลงใช่มั้ยล่ะ"
    n "ก็เหมือนความทรงจำที่ยิ่งเวลาผ่านไปนานมากเท่าไหร่ ความทรงจำก็จะยิ่งเลือนลางมากเท่านั้น"
    show nut casual smile
    n "นี่เธอ..."
    n "โดนอะไรกระแทกหัวมารึเปล่า"
    show nut casual closed open angry with vpunch
    n "จะบ้ารึไงยะ!"
    show nut casual closed frown
    n "อะแฮ่ม"
    show nut casual frown
    n "ฉันแค่ลองคิดตามความหมายของเพลงที่ฟังเมื่อคืนน่ะ"
    n "รู้มั้ยว่าคนเรามีชีวิตอยู่ได้ประมาณ 80 ปี ถ้าเปรียบเทียบเป็นฟิล์มก็จะมีความยาวตั้ง \n1.15 ล้านกิโลเมตรเลยนะ ชีวิตที่เหมือนจะยาวนานแต่จริงๆก็สั้นแค่นิดเดียวเอง"
    s "..."
    show nut casual open with dissolve
    n "เพราะงั้นเราควรจะทำทุกวินาทีให้มีค่าใช่มั้ยล่ะ"
    n "เพื่อให้ฟิล์มทุกแผ่นที่ถูกบันทึกด้วยดวงตาของเรามีความหมาย"
    show nut casual smile with dissolve
    s "..."
    show nut casual closed smile with dissolve
    s "(ไม่รู้เหมือนกันว่าทำไมแต่ผมรู้สึกว่าตัวเธอในตอนนั้นแตกต่างไปจากทุกครั้งที่ผ่านมา {w=3.0}คงเป็นเพราะพึ่งได้เห็นอีกด้านนึงที่เธอไม่ค่อยแสดงออกมาให้ใครเห็นล่ะมั้ง)"

    scene bg Street_Summer_Evening with Fade(0.5, 1.0, 0.5)
    show nut casual smile with dissolve
    s "นี่เธอทำไมเวลาอยู่กับฉันถึงชอบพูดอะไรแปลกๆหรอ"
    show nut casual frown
    n "แปลกๆ? แปลกแบบไหนหรอ"
    s "ก็อะไรที่มันจริงๆจังๆ ดูเป็นปรัชญา อะไรประมาณนั้นน่ะ"
    s "ตอนอยู่กับเพื่อนคนอื่นไม่เคยเห็นเธอพูดเรื่องแบบนี้เลย"
    n "อ๋อ...{w=1.0}เรื่องนั้นเองหรอ"
    show nut casual open
    n "ก็เพราะฉันคิดว่าพวกนายน่าจะเป็นคนไม่กี่คนที่ฟังเรื่องที่ฉันพูดได้โดยไม่ตัดสินน่ะ"
    show nut casual frown
    n "ถ้าเป็นคนอื่นๆเขาคงจะชินกับภาพลักษณ์ที่ฉันแสดงออกมาในห้องจนไม่คิดว่า\nฉันจะพูดเรื่องอะไรแบบนี้ออกมาได้ {w=1.5}หรือพอพูดออกไปแล้วพวกเขาก็จะคิดว่ามัน\nดูตลกหรือดูไม่จริงจัง"
    show nut casual smile with dissolve
    n "ทั้งๆที่ฉันก็พูดออกมาจากใจจริงแท้ๆ"
    show nut casual frown
    n "บางคนน่ะนะ ไม่ว่าฉันจะพูดอะไรก็ตามพวกเขาจะเข้าข้างฉันโดยที่\nไม่สนถูกผิดอะไรเลย"
    show nut casual open with dissolve
    n "แต่พวกนายเป็นคนที่ฉันสามารถพูดได้ทุกเรื่อง เป็นคนที่ยอมฟังฉันระบาย\nเรื่องไร้สาระออกมาได้โดยไม่ตัดสินและก็ไม่เข้าข้างฉัน"
    n "เพราะงั้นพวกนายก็เลยเป็นเซฟโซนสำหรับฉันยังไงล่ะ"
    show nut casual smile with dissolve
    pause 1.5

    scene bg BusStop_Summer_Afternoon with fade
    show nut casual open with dissolve
    n "ส่งฉันตรงนี้ก็ได้นะ ฉันโทรบอกให้ที่บ้านมารับแล้ว"
    show nut casual smile
    s "โอเค งั้นก็เดินทางปลอดภัยนะ"
    show nut casual closed smile
    n "อื้ม นายก็เช่นกันนะ"
    show nut casual open
    n "วันนี้ขอบคุณนะที่ยอมไปดูหนังเป็นเพื่อนฉัน สนุกมากๆเลยล่ะ"
    show nut casual closed open
    n "ไว้คราวหน้าไปดูด้วยกันอีกนะ"
    show nut casual smile
    s "..."
    show nut casual frown with dissolve
    s "ได้สิ"
    show nut casual closed smile with dissolve
    pause 1.5

    scene bg Livingroom_Night with fade
    play audio "audio/iPhone Notification Vibrate Sound Effect.mp3"
    "{i}ครืดๆ{/i}"
    s "?"
    nvl clear
    k_nvl "ไงพ่อเทพบุตร กลับบ้านโดยสวัสดิภาพมั้ย"
    s_nvl "เออ พึ่งถึงเนี่ย"
    k_nvl "อ๋ออ พึ่งถึงด้วย"
    k_nvl "แสดงว่าไปเดินเล่นกับเขามา\nใช่มั้ยเนี่ย"
    s_nvl "ไม่ใช่โว๊ยย"
    s_nvl "ส่งแค่ป้ายรถเมล์แล้วก็กลับ ที่พึ่งถึงเพราะฉันแวะซื้อของ\nต่างหาก"
    k_nvl "แค่ไปส่งเองหรอเนี่ย ผิดหวังชะมัด"
    s_nvl "นี่นาย..."
    s_nvl "ตอนนั้นไม่ได้มีคนมารับ\nจริงๆใช่มั้ย"
    k_nvl "ไม่บอกหรอก ความลับทางราชการ"
    s_nvl "..."
    k_nvl "ได้เห็นเพื่อนรักมีความสุข\nทั้งทีแค่นี้จิ๊บจ๊อยน่า"
    s_nvl "ให้ตายสิ"

    $ nvl_hide(dissolve)
    stop music fadeout 1.5
    pause 1.5

    jump festival


label festival:
    play music "audio/Sketchbook 2024-09-25.ogg" fadein 0.5
    scene black with fade
    pause 3.0
    scene bg School_Hallway_Day with fade

    show nut uni open with dissolve
    n "เย็นนี้มีงานเทศกาลด้วยล่ะ พวกเราไปเที่ยวกันเถอะ"
    hide nut uni open with dissolve
    show keng uni smile with dissolve
    k "ได้ข่าวว่าจะมีจุดพลุกันด้วยนะ ไปด้วยกันมั้ยชิน"
    s "ไปอยู่แล้ว ไปหาของกินอร่อยๆกินกันเถอะ"
    hide keng uni smile with dissolve
    show nut uni open with dissolve
    n "งั้นเจอกันที่ป้ายรถเมล์ตอนห้าโมงครึ่งนะ"

    scene bg BusStop_Summer_Afternoon with Fade(0.5, 1.5, 0.5)
    show keng uni smile with dissolve
    k "โย่ว ชิน"
    s "ไงเก่ง นัทยังไม่มาหรอ"
    k "ยังไม่เห็นเลยนะ สงสัยจะแต่งสวยอยู่มั้ง"
    n "นี่พวกนายย!"
    show keng uni smile with move:
        xalign 0.3
        yalign 1.0
    show nut uni smile with easeinright:
        xalign 0.7
        yalign 1.0
    k "โอ๊ะ คุณนายเสด็จแล้ว"
    k "เราไปกันเลยดีมั้ย"
    s "อื้ม ไปกันเถอะ"

    scene bg Street_Summer_Stars with Fade(0.5, 1.0, 0.5)
    pause 3.0

    scene bg Old_FestivalB with Fade(0.5, 1.0, 0.5)
    show keng uni smile with dissolve
    k "ของกินเยอะจนเลือกไม่ถูกเลยแหะ"
    s "นึกถึงสมัยก่อนเลยเนาะ"
    show keng uni open
    k "อ๋อ ตอนที่ไปเที่ยวกันแถวบ้านฉันน่ะหรอ"
    show keng uni frown
    s "สนุกมากเลยเนาะตอนนั้น"
    s "แถวบ้านนายแท้ๆแต่พากันหลงเกือบหลับบ้านไม่ได้แหนะ"
    show keng uni smile
    k "ฮ่าๆๆๆ"
    k "ยังดีนะกลับมาครบ 32"
    k "ว่าแต่นัทไปไหนแล้วนะ"
    s "คงจะไปซื้อของล่ะมั้ง เดี๋ยวก็กลับมา"

    hide keng uni smile with dissolve
    show nut uni closed open with dissolve
    k "กลับมาแล้วจ้า~"
    show nut uni smile
    s "เดินไปคนเดียวเดี๋ยวก็หลงทางหรอกยัยบ๊อง"
    show nut uni closed open angry with vpunch
    n "คิดว่าฉันเตี้ยกว่านายแล้วจะซัดหน้านายไม่ได้หรอตาบ้า"
    s "แต่ฉันวิ่งไวกว่าเธอนะ ก่อนจะซัดหน้าวิ่งตามฉันให้ทันก่อนเถอะ"
    hide nut uni closed open angry with dissolve 
    show keng uni smile with dissolve
    k "..."
    k "พวกนายนี่น้า~"
    k "อย่าลืมส่งการ์ดเชิญมาให้ฉันด้วยล่ะ"
    with vpunch
    s "ไอ้นี่ก็ชงอย่างเดียวเลยโว๊ยย"

    play sound "audio/Fireworks sound effect.mp3" loop

    show keng uni frown with dissolve
    k "?"
    show keng uni open
    k "เริ่มจุดพลุกันแล้วล่ะ"
    hide keng uni open with dissolve
    pause 1.5
    scene bg Old_FestivalC with dissolve
    pause 1.5
    s "ไม่ได้มาดูพลุใกล้ๆแบบนี้นานแล้วแหะ"
    k "นั่นสินะ"
    hide keng uni smile with dissolve
    show nut uni closed open with dissolve
    n "นี่ๆ เรามาถ่ายรูปกันเถอะ"
    show nut uni open
    n "แบ็กกราวนด์เป็นดอกไม้ไฟด้วยน่าจะเริ่ดมากเลยแหละ"
    show nut uni smile
    s "เดี๋ยวฉันถ่ายเซลฟีให้ มายืนใกล้ๆกันนะ"
    show nut uni smile with move:
        xalign 0.7
        yalign 1.0
    show keng uni smile with dissolve
    show keng uni smile with move:
        xalign 0.3
        yalign 1.0

    s "พร้อมนะทุกคน นับ"
    s "3"
    s "2"
    s "1"

    scene white with None
    stop sound fadeout 0.5
    stop music fadeout 0.5
    play audio "audio/Camera flash sound effect.mp3"
    pause(5.0)

    jump the_conclusion

label the_conclusion:
    scene black with fade
    play music "audio/Ludum Dare 30 05.ogg" fadein 1.5 fadeout 1.5 noloop
    s "..."
    show nut uni smile with dissolve
    n "..."
    s "นัทหรอ"
    show nut uni closed smile
    n "อื้ม"
    show nut uni smile
    menu where_are_we:
        " "
        "เธอมาทำอะไรที่นี่":
            show nut uni closed smile with dissolve
            n "ฉันแค่อยากเจอนายเฉยๆน่ะ"
            n "ไม่ได้เจอเพื่อนสนิทตั้งนาน "

            menu where_are_we_loop:
                " "
                "นี่เราอยู่ที่ไหนกัน":
                    pass

        "นี่เราอยู่ที่ไหนกัน":
            pass
        
    s "นี่เราอยู่ที่ไหนกัน ทำไมทุกอย่างมันถึงได้มืดจนมองไม่เห็นอะไรเลย"
    show nut uni smile with dissolve
    n "..."
    show nut uni open with dissolve
    n "เราอยู่ที่ฉากสุดท้ายของหนังเรื่องนี้ยังไงล่ะชิน"
    n "หนังที่นายเป็นคนเขียนบทเอง กำกับเอง และบันทึกทุกฉากด้วยตัวของนายเอง {p}{size=-5}{alpha=0.5}ลึกๆแล้วนายก็รู้ว่าเรื่องราวบทนี้มันจะจบยังไง{/alpha}{/size}"
    show nut uni closed open blush with dissolve
    n "ฉันดีใจนะที่นายให้ฉันเป็นตัวเอกในเรื่องราวของนาย {p}และฉันก็ดีใจมากๆเลยที่มีนายเป็นตัวเอกในเรื่องราวของฉัน"
    show nut uni open with dissolve
    n "ถึงแม้ว่าจะเป็นเพียงระยะเวลาสั้นๆที่พวกเราได้เดินบนเส้นทางเดียวกัน แต่สำหรับฉันช่วงเวลาเหล่านั้นมันมีความหมายมากๆเลยล่ะ"
    n "เรื่องบางเรื่องจะเกิดขึ้นไม่ได้เลยถ้าไม่มีนายอยู่ข้างๆฉัน ขอบคุณที่คอยอยู่เคียงข้างฉันในทุกช่วงเวลานะชิน ฉันดีใจมากๆเลยล่ะ"
    show nut uni smile with dissolve
    n "ขอบคุณที่เป็นเพื่อนที่ดีกับฉันเสมอมานะ"
    show nut uni smile b with dissolve
    n "ต่อจากนี้ก็ขอให้นายโชคดีกับเรื่องราวใหม่ๆในชีวิตของนายนะ ถ้าวันข้างหน้าเจออะไรสนุกๆก็อย่าลืมแวะมาเล่าให้ฉันฟังด้วยล่ะ"
    show nut uni closed smile b with dissolve
    n "ฉันจะรอฟังนะ"
    show nut uni smile b with dissolve
    n "ขอบคุณสำหรับทุกอย่างนะชิน และก็..."
    show nut uni closed open b with dissolve
    n "Sayonara (ลาก่อนนะ)"
    $ _skipping = False
    $ quick_menu = False
    scene white with dissolve
    stop music
    pause 1.5
    play sound "audio/Old Movie The End Film With Sound Effect HD FREE.mp3"
    $ renpy.pause(7.0, hard=True)
    scene bg Old_School with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg School_Hallway_Day with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg Classroom_Day with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg Backstreet_Spring_Afternoon with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg Street_Spring_Evening with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg BusStop_Spring_Afternoon with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg Restaurant_B with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene bg Old_FestivalC with Dissolve(1.5)
    $ renpy.pause(5.0, hard=True)
    scene white with Fade(0.5, 0.0, 3.0)
    play sound "audio/Digital alarm clock sound.mp3"
    pause 1.5
    scene bg Bedroom_Day with Dissolve(5.0)
    $ _skipping = True
    $ quick_menu = True
    play music "audio/VGMA Challenge 19.ogg" fadein 1.5
    s "..."
    s "(ผมค่อยๆลืมตาตื่นจากความฝันที่ยาวนาน ไม่รู้สึกตัวเลยว่าเวลาผ่านไป\nนานแค่ไหนแล้ว)"
    s "(พอผมลุกขึ้นนั่งที่ข้างเตียงภาพจากความฝันก็ค่อยๆเลือนหายไป\nและทิ้งไว้เพียงความรู้สึกที่ไม่อยากให้ความฝันนั้นจบลง)"
    window hide
    
    scene bg BusStop_Spring_Day with fade
    show keng casual open with dissolve
    k "เมื่อวานนายหายไปไหนมา ส่งข้อความไปก็ไม่ตอบ โทรไปก็ไม่รับ"
    show keng casual frown
    s "เมื่อวาน?"
    show keng casual open
    k "เมื่อวานนายไม่มาทำงาน พอฉันโทรไปหานายนายก็ไม่รับ \nฉันส่งข้อความไปนายก็ไม่ตอบ"
    show keng casual frown
    s "ขอโทษนะ ฉันจำอะไรไม่ค่อยได้เลยน่ะ จำได้แค่ว่ากำลังนั่งรถไฟกลับบ้าน\nแล้วภาพก็ตัดไปเลย"
    k "..."
    show keng casual open
    k "ชิน นายโหมงานหนักเกินไปแล้วนะ"
    k "ฉันรู้ว่างานนี้มันสำคัญกับนายมากแต่ดูจากสภาพร่างกายตอนนี้แล้ว\nนายทำแบบนี้ต่อไปได้อีกไม่นานหรอก"
    show keng casual frown
    s "..."
    show keng casual open
    k "เชื่อฉันเถอะนะชิน ฉันเตือนเพราะฉันเป็นห่วงนายนะ"
    show keng casual smile
    s "ขอบใจนะเก่ง"

    scene bg Train_Day with fade
    pause 3.0
    scene bg City_Morning with fade
    pause 3.0
    scene black with fade

    centered "{color=#ffffff}{size=+40}12:00{/size}{/color}"

    scene bg Restaurant_B with fade
    show keng casual smile with dissolve

    k "เมื่อวานฉันไปร้านหนังสือมา ไปเจอเล่มนึงน่าสนใจมาด้วยล่ะ"
    k "อะ นี่"
    s "?"
    s "นี่มันเรื่องที่เราไปดูกันตอนนั้นไม่ใช่หรอ"
    k "ฉันไปเจอมาที่ร้านหนังสือน่ะก็เลยซื้อมาอ่าน"
    k "ฉันให้นายยืมอ่านก็ได้นะ"
    s "ขอบคุณนะเก่ง"
    s "น่าคิดถึงจังเลยนะตอนม.ปลายเนี่ย"
    show keng casual frown
    k "..."
    show keng casual open
    k "นี่ชิน"
    show keng casual frown
    s "?"
    show keng casual smile
    k "สุดสัปดาห์นี้ไปเยี่ยมนัทกันมั้ย"
    s "..."
    s "อือ ไปสิ"

    scene black with fade
    pause 3.0

    scene bg Temple_Spring_Day with dissolve
    k "ไม่ได้มาที่นี่นานเหมือนกันนะ"
    s "ครั้งล่าสุดน่าจะปีที่แล้วล่ะมั้ง"
    s "เวลาผ่านไปไวจังเลยนะ"

    scene bg Old_FuneralNut with Fade(0.5, 1.5, 1.5)
    pause 0.5
    window show
    s "5 ปีแล้วสินะ"
    s "รู้สึกเหมือนเธอพึ่งจากไปเมื่อวานนี้เอง"
    k "ถ้าเธอยังอยู่ เธอจะพูดกับพวกเราว่ายังไงกันนะ"
    s "คงจะสวดพวกเรายับเลยล่ะ เอาแต่นั่งก้มหน้าก้มตาทำงานซังกะตายไปวันๆ \nไม่ออกไปใช้ชีวิตบ้างเลย"
    k "ฮ่าๆๆ คำพูดสมกับเป็นนัทจริงๆนั่นแหละ"
    s "น่าคิดถึงจังเลยนะ"
    k "..."
    k "อย่าทำหน้าเศร้าแบบนั้นสิชิน มาเจอเธอทั้งทียิ้มเข้าไว้เถอะน่า"
    s "..."
    k "เธอคนนั้นไม่อยากให้นายเศร้าหรอกนะ"
    s "นั่นสินะ"
    s "ขอบคุณนะเก่ง"
    window hide

    $ quick_menu = False
    $ _skipping = False
    scene white with Dissolve(3.0)
    pause 1.5
    centered "หลังจากจบการศึกษาได้ไม่นาน นัทก็จากไปด้วยโรคประจำตัว"
    centered "สำหรับผม แม้จะเป็นเพียงช่วงเวลาสั้นๆที่ได้พบกับเธอคนนั้นแต่ผมก็รู้สึกได้ว่าตัวเองเปลี่ยนไปจากเดิมมากจริงๆ"
    centered "เธอคนนั้นผู้แต่งเติมสีสันให้ชีวิตช่วงมัธยมปลายของผมมีชีวิตชีวามากกว่าเก่า"
    centered "แม้เวลาจะผ่านล่วงเลยไปหลายปี แต่ผมก็ยังคงคิดถึงคำพูดที่เธอเคยบอกกับผมในวันนั้น"
    centered "คนเรามีชีวิตอยู่ได้ประมาณ 80 ปี ถ้าเปรียบเทียบเป็นฟิล์มก็จะมีความยาวราว 1.15 ล้านกิโลเมตร\nชีวิตที่ดูเหมือนจะยาวไกลแต่ความจริงก็สั้นแค่นี้เอง"
    centered "แม้ช่วงเวลาที่เราพบกันจะเป็นเพียงช่วงสั้นๆ แต่ฟิล์มที่บันทึกภาพความทรงจำของเธอผู้นั้นจะไม่มีวันลบเลือนไปจากผมอย่างแน่นอน"
    centered "แม้นี่จะไม่ใช่ตอนจบของเรื่องราวที่ผมคาดหวังไว้ แต่อย่างน้อยก็ทำให้ผมได้รู้ว่าครั้งนึงเคยมีความสุขมากแค่ไหน"
    centered "ขอบคุณสำหรับทุกอย่างที่ผ่านมานะนัท"
    centered "และก็"
    centered "ไว้เจอกันใหม่นะ"

    centered "THE END"
    
    scene black with Fade(1.5, 1.0, 1.5)
    stop music fadeout 3.0
    $ renpy.pause(3.0, hard=True)

    return
    