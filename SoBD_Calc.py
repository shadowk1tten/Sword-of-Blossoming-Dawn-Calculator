import itertools
import tkinter as tk
from tkinter import ttk
import ttkwidgets
from tktooltip import ToolTip
import sv_ttk
import pywinstyles
import base64
import os

#Augment Dictionary
augment_dict = {
    'ADAPt' : False,
    'All For You' : False,
    'Back to Basics' : False,
    'Blunt Force' : False,
    'Celestial Body' : False,
    'Critical Healing' : False,
    'Critical Rythm' : False,
    'Deft' : False,
    'Double Tap' : False,
    'Dual Wield' : False,
    'Empyrean Promise' : False,
    'EscAPADe' : False,
    'First Aid Kit' : False,
    'Golden Spatula' : False,
    'Goliath' : False,
    'Hand of Baron' : False,
    'Hat on a Hat' : False,
    'Heavy Hitter' : False,
    'Im a Baby Kitty Where is Mama' : False,
    'Jeweled Gauntlet' : False,
    'Lightning Strikes' : False,
    'Mad Scientist' : False,
    'Marksmage' : False,
    'Overflow' : False,
    'Phenomenal Evil' : False,
    'Protein Shake' : False,
    'Slap Around' : False,
    'Symphony of War' : False,
    'Tap Dancer' : False,
    'Twice Thrice' : False,
    'Typhoon' : False,
    'Upgrade Sword of Blossoming Dawn' : False,
    'Witchful Thinking' : False,
    'Wooglets Witchcap' : False,
    'Zealot' : False,
}

# [ad, ap, atks, h&s, crit, mana regen,health,mana,armor,mr]
all_items = {
    'Blossom' : [0,45,0,12,0,0,0,0,0,0],
    'Moonstone' : [0,25,0,0,0,125,200,0,0,0],
    'Nashors' : [0,80,50,0,0,0,0,0,0,0],
    'Phantom' : [0,0,65,0,25,0,0,0,0,0],
    'Runaans' : [0,0,40,0,25,0,0,0,0,0],
    'Diadem' : [0,0,0,13,0,100,200,1000,0,0],
    'Helia' : [0,35,0,0,0,125,200,0,0,0],
    'Ardent' : [0,45,25,10,0,125,0,0,0,0],
    'Dawncore' : [0,45,0,16,0,100,0,0,0,0],
    'Guinsoos' : [30,30,57,0,0,0,0,0,0,0],
    'Staff' : [0,80,0,10,0,125,0,0,0,0],
    'Rite' : [0,50,0,0,45,0,0,0,0,0],
    'Rabadon' : [0,130,0,0,0,0,0,0,0,0],
    'Yuntal' : [50,0,70,0,25,0,0,0,0,0],
    'Terminus' : [30,0,35,0,0,0,0,0,24,24],
    'Zhonyas' : [0,105,0,0,0,0,0,0,50,0],
    'Dance' : [60,0,0,0,0,0,0,0,50,0],
    'Wooglets' : [0,300,0,0,0,0,0,0,50,0],
    'Spatula' : [90,125,60,0,25.200,350,350,40,40],
    'Bork' : [40,0,25,0,0,0,0,0,0,0]
}

# the machine.
def calculate_optimal():
    active_augs = []
    active_augs.append(augment_select1.get())
    active_augs.append(augment_select2.get())
    active_augs.append(augment_select3.get())
    active_augs.append(augment_select4.get())
    active_augs.append(augment_select5.get())
    for key in augment_dict:
        augment_dict[key] = False
    for aug in active_augs:
        if aug != 'Select Augment':
            augment_dict[aug] = True
    items = ['Moonstone','Runaans','Ardent','Guinsoos','Dawncore','Diadem','Nashors','Phantom','Helia','Staff','Rite','Rabadon','Yuntal','Terminus','Zhonyas','Dance','Bork']
    item_count = 5
    if asboots_on.get() == True:
        item_count -= 1
    if augment_dict['Wooglets Witchcap'] == True:
        item_count -= 1
    if augment_dict['Golden Spatula'] == True:
        item_count -= 1
    item_sets = list(itertools.combinations(items,item_count))
    highest_hps = 0
    for items in item_sets:
        totalstats = [0,0,0,0,0,0,0,0,0,0]
        apmod = 1
        admod = 1
        hpmod = 1
        onhitmult = 1
        items += ('Blossom',)
        if augment_dict['Wooglets Witchcap'] == True:
            if 'Zhonyas' in items:
                pass
            if 'Rabadon' in items:
                pass
            else:
                items += ('Wooglets',)
        if augment_dict['Golden Spatula'] == True:
            items += ('Spatula',)
        for item in items:
            for stat in range(9):
                statadd = all_items[item][stat]
                totalstats[stat] += statadd
# separate stats
        ad_bonus = totalstats[0]
        if ad_entry.get().isdigit():
            ad_bonus += int(ad_entry.get())
        ap_total = totalstats[1]
        if ap_entry.get().isdigit():
            ap_total += int(ap_entry.get())
        as_total = totalstats[2]
        if as_entry.get().isdigit():
            as_total += int(as_entry.get())
        hsp_total = totalstats[3]
        if hsp_entry.get().isdigit():
            hsp_total += int(hsp_entry.get())
        crit = totalstats[4]
        if crit_entry.get().isdigit():
            crit += int(crit_entry.get())
        mana_regen = totalstats[5]
        bonus_health = totalstats[6]
        bonus_mana = totalstats[7]
        armor_total = totalstats[8]
        if armor_entry.get().isdigit():
            armor_total += int(armor_entry.get())
        mr_total = totalstats[9]
        if mr_entry.get().isdigit():
            mr_total += int(mr_entry.get())
# health/resists
        if augment_dict['Celestial Body'] == True:
            bonus_health += 1500
        if augment_dict['Mad Scientist'] == True:
            if madsci_small.get() == True:
                hpmod += 0.2
        if augment_dict['Goliath'] == True:
            hpmod += 0.35
        bonus_health *= hpmod
        if augment_dict['Hat on a Hat'] == True:
            if hat_entry.get().isdigit():
                mr_total += 4*int(hat_entry.get())
# ap/ad conversions
        if augment_dict['ADAPt'] or augment_dict['EscAPADe'] == True:
            if augment_dict['ADAPt'] == True:
                if augment_dict['Blunt Force'] == True:
                    admod += 0.2
                if augment_dict['Goliath'] == True:
                    apmod += 0.15
                if augment_dict['Hand of Baron'] == True:
                    apmod += 0.25
                if augment_dict['Mad Scientist'] == True:
                    if madsci_small.get() == False:
                        apmod += 0.3
                if augment_dict['Slap Around'] == True:
                    if slap_entry.get().isdigit():
                        ap_total += 10*int(slap_entry.get())
                if augment_dict['Hat on a Hat'] == True:
                    if hat_entry.get().isdigit():
                        ap_total += 8*int(hat_entry.get())
                if augment_dict['Phenomenal Evil'] == True:
                    if phenomenal_entry.get().isdigit():
                        ap_total += int(phenomenal_entry.get())
                if 'Rabadon' in items:
                    apmod += 0.30
                    if augment_dict['Wooglets Witchcap'] == True:
                        apmod += 0.2
                if 'Dawncore' in items:
                    ap_total += mana_regen/10
                if augment_dict['Witchful Thinking'] == True:
                    ap_total += 80
                ad_total = ad_bonus + 100
                ad_total *= admod
                apmod += 0.15
                ap_total += ad_total/0.6
                ad_total = 100
                ap_total *= apmod
            if augment_dict['EscAPADe'] == True:
                if augment_dict['Blunt Force'] == True:
                    admod += 0.2
                if 'Rabadon' in items:
                    apmod += 0.3
                    if augment_dict['Wooglets Witchcap'] == True:
                        apmod += 0.2
                if 'Dawncore' in items:
                    ap_total += mana_regen/10
                if augment_dict['Goliath'] == True:
                    admod += 0.15
                if augment_dict['Hand of Baron'] == True:
                    admod += 0.25
                if augment_dict['Mad Scientist'] == True:
                    if madsci_small.get() == False:
                        admod += 0.3
                if augment_dict['Slap Around'] == True:
                    if slap_entry.get().isdigit():
                        ad_bonus += 6*int(slap_entry.get())
                if augment_dict['Hat on a Hat'] == True:
                    if hat_entry.get().isdigit():
                        ap_total += 8*int(hat_entry.get())
                if augment_dict['Phenomenal Evil'] == True:
                    if phenomenal_entry.get().isdigit():
                        ap_total += int(phenomenal_entry.get())
                if augment_dict['Witchful Thinking'] == True:
                    ap_total += 80
                ap_total *= apmod
                admod += 0.15
                ad_bonus += ap_total*0.66
                ap_total = 0
                ad_total = ad_bonus + 100
                ad_total *= admod
# not adapt or escapade
        else:
            if 'Dawncore' in items:
                ap_total += mana_regen/10
            if 'Rabadon' in items:
                    apmod += 0.3
                    if augment_dict['Wooglets Witchcap'] == True:
                        apmod += 0.2
            if augment_dict['Blunt Force'] == True:
                admod += 0.2
            if augment_dict['Mad Scientist'] == True:
                if madsci_small.get() == False:
                    if ap_total > ad_bonus:
                        apmod += 0.3
                    else:
                        admod +=0.3
            if augment_dict['Goliath'] == True:
                if ap_total > ad_bonus:
                    apmod += 0.15
                else:
                    admod += 0.15
            if augment_dict['Hand of Baron'] == True:
                if ap_total > ad_bonus:
                    apmod += 0.25
                else:
                    admod += 0.25
            if augment_dict['Slap Around'] == True:
                if slap_entry.get().isdigit():
                    if ap_total > ad_bonus:
                        ap_total += 10*int(slap_entry.get())
                    else:
                        ad_bonus += 6*int(slap_entry.get())
            if augment_dict['Hat on a Hat'] == True:
                if hat_entry.get().isdigit():
                    ap_total += 8*int(hat_entry.get())
            if augment_dict['Phenomenal Evil'] == True:
                if phenomenal_entry.get().isdigit():
                    ap_total += int(phenomenal_entry.get())
            if augment_dict['Witchful Thinking'] == True:
                    ap_total += 80
            ad_total = ad_bonus + 100
            ad_total *= admod
            ap_total *= apmod
# extra bonuses
        if augment_dict['Tap Dancer'] == True:
            as_total += 35
        if augment_dict['Upgrade Sword of Blossoming Dawn'] == True:
            as_total += 100
        if 'Dawncore' in items:
            hsp_total += mana_regen/50
        if 'Diadem' in items:
            hsp_total += (bonus_mana+1000)/200
        if augment_dict['Empyrean Promise'] == True:
            hsp_total += 15
        if asboots_on.get() == True:
            as_total += 25
        if augment_dict['Critical Healing'] == True:
            crit += 25
        if augment_dict['Protein Shake'] == True:
            hsp_total += 25 + 0.35*mr_total + 0.35*armor_total
        if augment_dict['Critical Rythm'] == True:
            crit += 25
            as_total += 60
        if augment_dict['Deft'] == True:
            as_total += 60
        if augment_dict['First Aid Kit'] == True:
            hsp_total += 20
        if augment_dict['Im a Baby Kitty Where is Mama'] == True:
            hsp_total += 50
        if augment_dict['Jeweled Gauntlet'] == True:
            crit += 25 + 0.00045*ap_total
        if augment_dict['Zealot'] == True:
            as_total += 35 + 0.05*ap_total
            crit += 25 + 0.05*ap_total
        as_total += hsp_total*1.2
        as_total = as_total/100
        as_total = 0.64 + (as_total + 0.025 * 17 * (0.7025 + 0.0175 * 17)) * 0.65
        if augment_dict['Lightning Strikes'] == True:
            as_total *= 1.2
        if augment_dict['Dual Wield'] == True:
            as_total *= 1.1
        crit /= 100
        if crit > 1:
            crit = 1
        hsp_total = hsp_total/100 + 1
# Healing
        healonhit = (0.1*ad_bonus + 0.07*ap_total)
        addative_hps = 0
        onhit = 0
        helia_store = 0
        if 'Diadem' in items:
            addative_hps += bonus_mana*0.008
# Helia
        if 'Helia' in items:
            ad_damage = (ad_total*(round(adeff_slider.get(),0)/100)) + crit * (2-1) * (ad_total*(round(adeff_slider.get(),0)/100))
            if 'Nashors' in items:
                onhit += ap_total*0.15 + 15
            if 'Bork' in items:
                onhit += 0.06*(int(round(borkslider.get(), 1))/2)
            if 'Ardent' in items:
                onhit += 20
            if 'Terminus' in items:
                onhit += 30
            if augment_dict['Lightning Strikes'] == True:
                if as_total >= 1.75:
                    onhit += 40
            if 'Guinsoos' in items:
                onhit += 30
                onhit *= 1.333
            if augment_dict['Marksmage'] == True:
                onhit += (ap_total*0.75)*adeff_slider.get()
            if augment_dict['Heavy Hitter'] == True:
                onhit += (bonus_health + 2300)*0.035
            helia_store = (ad_damage + (onhit*round(adeff_slider.get())))*0.35
            if augment_dict['Celestial Body'] == True:
                helia_store *= 0.9
            if helia_store > 250:
                helia_store = 250
            helia_store *= as_total
# onhit buffs
        if 'Runaans' in items:
            healonhit += 2*(0.1*ad_bonus + 0.07*ap_total)
        if augment_dict['Typhoon'] == True:
            healonhit += (0.1*ad_bonus + 0.07*ap_total)
        if augment_dict['Double Tap'] == True:
            healonhit += (0.1*ad_bonus + 0.07*ap_total)*(1 + crit)
        if augment_dict['Dual Wield'] == True:
            healonhit += (0.1*ad_bonus + 0.07*ap_total)
        if augment_dict['Upgrade Sword of Blossoming Dawn'] == True:
            healonhit += ((0.1*ad_bonus + 0.07*ap_total)*1.5)*round(adeff_slider.get())
        if 'Guinsoos' in items:
            onhitmult += 0.33
        if augment_dict['Twice Thrice'] == True:
            onhitmult += 0.33
        healonhit *= onhitmult
# add up heals
        hps = (healonhit*as_total + addative_hps + helia_store)
# post bonus healing
        if 'Moonstone' in items:
            hps *= 1.3
        if augment_dict['Critical Healing'] == True:
            hps *= 1 + crit*0.4
        if augment_dict['Overflow'] == True:
            hps *= 1.10 + 0.00005*(bonus_mana+1000)
        if augment_dict['All For You'] == True:
            hps *= 1.3
        if augment_dict['Back to Basics'] == True:
            hsp_total *= 1.3
        hps *= hsp_total
        hps /= 2
# Get Highest Healing Per Second
        if hps > highest_hps:
            highest_hps = hps
            best_items = items
    highest_hps = round(highest_hps,1)
    build_label_var.set(best_items)
    hps_label_var.set('Healing per second: ' + str(highest_hps))

# tkinter window
root = tk.Tk()
root.title('Mathematically Correct Sword of Blossoming Dawn')
root.resizable(0,0)

# icon data
icon = \
    '''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
    '''
icondata = base64.b64decode(icon)
tempfile = 'sword.ico'
iconfile = open(tempfile, 'wb')
iconfile.write(icondata)
iconfile.close()
root.wm_iconbitmap(tempfile)
os.remove(tempfile)

pywinstyles.change_header_color(root, '#1c1c1c')

augment_list = ['ADAPt','All For You','Back to Basics','Blunt Force','Celestial Body','Critical Healing','Critical Rythm','Deft','Double Tap','Dual Wield','Empyrean Promise','EscAPADe','First Aid Kit','Golden Spatula','Goliath','Hand of Baron','Hat on a Hat','Heavy Hitter','Im a Baby Kitty Where is Mama','Jeweled Gauntlet','Lightning Strikes','Mad Scientist','Marksmage','Overflow','Phenomenal Evil','Protein Shake','Slap Around','Symphony of War','Tap Dancer','Twice Thrice','Typhoon','Upgrade Sword of Blossoming Dawn','Witchful Thinking','Wooglets Witchcap','Zealot']

# Options/Modifiers
class options(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Options', padding=15)

        global asboots_on
        asboots_on = tk.BooleanVar(self, False)
        global madsci_small
        madsci_small = tk.BooleanVar(self, False)

        self.add_widgets()

    def add_widgets(self):

        def madsci_toggle():
            global madsci_button
            global madsci_small
            if madsci_small.get() == True:
                madsci_button.config(text='Big')
                madsci_small = tk.BooleanVar(self, False)
            else:
                madsci_button.config(text='Small')
                madsci_small = tk.BooleanVar(self, True)

        def borkupdate(a):
            bork_label.config(text='Target max Health: ' + str(int(round(borkslider.get(),-1))))

        def adeffupdate(a):
            adeff_label.config(text='Combat Coefficient: ' + str(int(round(adeff_slider.get(), 0))) + '%')

        asboots_check = ttk.Checkbutton(self, text='Use Attack Speed Boots', variable=asboots_on)
        asboots_check.grid(row=1, column=0, columnspan=5, pady=5, sticky='w')

        as_tip = ttk.Label(self, text='(?)')
        as_tip.grid(row=1,column=1, sticky='e')

        ToolTip(as_tip, delay=0.25, msg='Slots in boots instead of a 6th item. Note that a 6th item instead of boots can increase healing by 30% - 50%')

        bork_label = ttk.Label(self, text='Target max Health: 3000')
        bork_label.grid(row=2, column=0, columnspan=5, pady=5, sticky='w')

        bork_tip = ttk.Label(self, text='(?)')
        bork_tip.grid(row=2, column=1, sticky='e')

        ToolTip(bork_tip, delay=0.25, msg='Take average max HP between enemy frontlines to calculate bork effectiveness')

        global borkslider
        borkslider = ttk.Scale(self, from_=2000, to=10000, orient='horizontal',command=borkupdate, value=3000)
        borkslider.grid(row=3, column=0, columnspan=5, pady=(5,10), sticky='ew')

        adeff_label = ttk.Label(self, text='Combat Coefficient: 70%')
        adeff_label.grid(row=4, column=0, columnspan=5, pady=5, sticky='w')

        adeff_tip = ttk.Label(self,text='(?)')
        adeff_tip.grid(row=4, column=1, sticky='e')

        ToolTip(adeff_tip, msg='Due to how Helia works, higher damage is better for in-combat healing, but worse for healing on waves. Increase value when fighting is more prominent, decrease when mainly farming waves', delay=0.25)

        global adeff_slider
        adeff_slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', command=adeffupdate, value=70)
        adeff_slider.grid(row=5,column=0,columnspan=5, pady=(5,10), sticky='ew')

        global madsci_button
        madsci_button = ttk.Checkbutton(self, text='Small', style='Toggle.TButton', command=madsci_toggle, variable=madsci_small, width= 5)
        madsci_button.grid(row=6, column=0, pady=(5, 10), sticky='nsew')

        madsci_label = ttk.Label(self, text='Mad Scientist State')
        madsci_label.grid(row=6, column=1, padx=10, sticky='ew')

        global slap_entry
        slap_entry = ttk.Entry(self,width=3)
        slap_entry.insert(0, 0)
        slap_entry.grid(row=7, column=0, pady=(5, 10), sticky='ew')

        slap_label = ttk.Label(self, text='Slap Around Stacks')
        slap_label.grid(row=7, column=1, padx=10, sticky='ew')

        global phenomenal_entry
        phenomenal_entry = ttk.Entry(self,width=3)
        phenomenal_entry.insert(0, 0)
        phenomenal_entry.grid(row=8, column=0, pady=(5, 10), sticky='ew')

        phenomenal_label = ttk.Label(self, text='Phenomenal Evil Stacks')
        phenomenal_label.grid(row=8, column=1, padx=10, sticky='ew')

        global hat_entry
        hat_entry = ttk.Entry(self,width=3)
        hat_entry.insert(0, 0)
        hat_entry.grid(row=9, column=0, pady=(5, 10), sticky='ew')

        hat_label = ttk.Label(self, text='Hat on a Hat Counter')
        hat_label.grid(row=9, column=1, padx=10, sticky='ew')

        hat_label = ttk.Label(self, text='(Count hat items as 2 hats)')
        hat_label.grid(row=10, column=0, columnspan=5, padx=10, sticky='ew')

# Augment Selection
class augment_box(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Augment Selection', padding=15)

        self.add_widgets()

    def add_widgets(self):

        updatelist1 = []
        updatelist2 = []
        updatelist3 = []
        updatelist4 = []
        updatelist5 = []

        def show_dropdown1(a):
            if augment_select1.get() == 'Select Augment':
                augment_select1.delete(0, tk.END)
                for i in augment_list:
                    augbox1.insert(tk.END, i)
            augbox1.place(x=5,y=35,width=180)
            augbox1.tkraise()
            if augbox1.get(0) != 'Select Augment':
                augbox1.insert(0, 'Select Augment')

        def show_dropdown2(a):
            if augment_select2.get() == 'Select Augment':
                augment_select2.delete(0, tk.END)
                for i in augment_list:
                    augbox2.insert(tk.END, i)
            augbox2.place(x=5,y=82,width=180)
            augbox2.tkraise()
            if augbox2.get(0) != 'Select Augment':
                augbox2.insert(0, 'Select Augment')

        def show_dropdown3(a):
            if augment_select3.get() == 'Select Augment':
                augment_select3.delete(0, tk.END)
                for i in augment_list:
                    augbox3.insert(tk.END, i)
            augbox3.place(x=5,y=129,width=180)
            augbox3.tkraise()
            if augbox3.get(0) != 'Select Augment':
                augbox3.insert(0, 'Select Augment')

        def show_dropdown4(a):
            if augment_select4.get() == 'Select Augment':
                augment_select4.delete(0, tk.END)
                for i in augment_list:
                    augbox4.insert(tk.END, i)
            augbox4.place(x=5,y=176,width=180,height=150)
            augbox4.tkraise()
            if augbox4.get(0) != 'Select Augment':
                augbox4.insert(0, 'Select Augment')

        def show_dropdown5(a):
            if augment_select5.get() == 'Select Augment':
                augment_select5.delete(0, tk.END)
                for i in augment_list:
                    augbox5.insert(tk.END, i)
            augbox5.place(x=5,y=223,width=180,height=100)
            augbox5.tkraise()
            if augbox5.get(0) != 'Select Augment':
                augbox5.insert(0, 'Select Augment')

        def hide_dropdown1(a):
            augment_select1.delete(0, tk.END)
            augment_select1.insert(0, augbox1.get(augbox1.curselection()))
            augbox1.place_forget()

        def hide_dropdown2(a):
            augment_select2.delete(0, tk.END)
            augment_select2.insert(0, augbox2.get(augbox2.curselection()))
            augbox2.place_forget()

        def hide_dropdown3(a):
            augment_select3.delete(0, tk.END)
            augment_select3.insert(0, augbox3.get(augbox3.curselection()))
            augbox3.place_forget()

        def hide_dropdown4(a):
            augment_select4.delete(0, tk.END)
            augment_select4.insert(0, augbox4.get(augbox4.curselection()))
            augbox4.place_forget()

        def hide_dropdown5(a):
            augment_select5.delete(0, tk.END)
            augment_select5.insert(0, augbox5.get(augbox5.curselection()))
            augbox5.place_forget()

        def list_update1(a):
            if entry1.get() != '':
                updatelist1 = []
                for i in range(0,len(augment_list)):
                    if entry1.get().lower() in augment_list[i].lower():
                        updatelist1.append(augment_list[i])
                augbox1.delete(0,tk.END)
                for i in updatelist1:
                    augbox1.insert(tk.END, i)
                if augbox1.get(0) != 'Select Augment':
                    augbox1.insert(0, 'Select Augment')
            else:
                augbox1.delete(0,tk.END)
                for i in augment_list:
                    augbox1.insert(tk.END, i)

        def list_update2(a):
            if entry2.get() != '':
                updatelist2 = []
                for i in range(0,len(augment_list)):
                    if entry2.get().lower() in augment_list[i].lower():
                        updatelist2.append(augment_list[i])
                augbox2.delete(0,tk.END)
                for i in updatelist2:
                    augbox2.insert(tk.END, i)
                if augbox2.get(0) != 'Select Augment':
                    augbox2.insert(0, 'Select Augment')
            else:
                augbox2.delete(0,tk.END)
                for i in augment_list:
                    augbox2.insert(tk.END, i)

        def list_update3(a):
            if entry3.get() != '':
                updatelist3 = []
                for i in range(0,len(augment_list)):
                    if entry3.get().lower() in augment_list[i].lower():
                        updatelist3.append(augment_list[i])
                augbox3.delete(0,tk.END)
                for i in updatelist3:
                    augbox3.insert(tk.END, i)
                if augbox3.get(0) != 'Select Augment':
                    augbox3.insert(0, 'Select Augment')
            else:
                augbox3.delete(0,tk.END)
                for i in augment_list:
                    augbox3.insert(tk.END, i)

        def list_update4(a):
            if entry4.get() != '':
                updatelist4 = []
                for i in range(0,len(augment_list)):
                    if entry4.get().lower() in augment_list[i].lower():
                        updatelist4.append(augment_list[i])
                augbox4.delete(0,tk.END)
                for i in updatelist4:
                    augbox4.insert(tk.END, i)
                if augbox4.get(0) != 'Select Augment':
                    augbox4.insert(0, 'Select Augment')
            else:
                augbox4.delete(0,tk.END)
                for i in augment_list:
                    augbox4.insert(tk.END, i)

        def list_update5(a):
            if entry5.get() != '':
                updatelist5 = []
                for i in range(0,len(augment_list)):
                    if entry5.get().lower() in augment_list[i].lower():
                        updatelist5.append(augment_list[i])
                augbox5.delete(0,tk.END)
                for i in updatelist5:
                    augbox5.insert(tk.END, i)
                if augbox5.get(0) != 'Select Augment':
                    augbox5.insert(0, 'Select Augment')
            else:
                augbox5.delete(0,tk.END)
                for i in augment_list:
                    augbox5.insert(tk.END, i)

        global augment_select1
        entry1 = tk.StringVar(self,'Select Augment')
        augment_select1 = ttk.Entry(self, textvariable=entry1)
        augment_select1.grid(row=0, column=0, padx=5, pady=(5,0), sticky='ew')
        augment_select1.bind('<KeyRelease>',list_update1)
        augment_select1.bind('<FocusIn>', show_dropdown1)

        augbox1 = tk.Listbox(self, selectmode=tk.SINGLE)
        augbox1.bind('<FocusIn>', hide_dropdown1)

        global augment_select2
        entry2 = tk.StringVar(self,'Select Augment')
        augment_select2 = ttk.Entry(self, textvariable=entry2)
        augment_select2.grid(row=1, column=0, padx=5, pady=(20,0), sticky='ew')
        augment_select2.bind('<KeyRelease>',list_update2)
        augment_select2.bind('<FocusIn>', show_dropdown2)

        augbox2 = tk.Listbox(self, selectmode=tk.SINGLE)
        augbox2.bind('<FocusIn>', hide_dropdown2)

        global augment_select3
        entry3 = tk.StringVar(self,'Select Augment')
        augment_select3 = ttk.Entry(self, textvariable=entry3)
        augment_select3.grid(row=2, column=0, padx=5, pady=(20,0), sticky='ew')
        augment_select3.bind('<KeyRelease>',list_update3)
        augment_select3.bind('<FocusIn>', show_dropdown3)

        augbox3 = tk.Listbox(self, selectmode=tk.SINGLE)
        augbox3.bind('<FocusIn>', hide_dropdown3)

        global augment_select4
        entry4 = tk.StringVar(self,'Select Augment')
        augment_select4 = ttk.Entry(self, textvariable=entry4)
        augment_select4.grid(row=3, column=0, padx=5, pady=(20,0), sticky='ew')
        augment_select4.bind('<KeyRelease>',list_update4)
        augment_select4.bind('<FocusIn>', show_dropdown4)

        augbox4 = tk.Listbox(self, selectmode=tk.SINGLE)
        augbox4.bind('<FocusIn>', hide_dropdown4)

        global augment_select5
        entry5 = tk.StringVar(self,'Select Augment')
        augment_select5 = ttk.Entry(self, textvariable=entry5)
        augment_select5.grid(row=4, column=0, padx=5, pady=(20,10), sticky='ew')
        augment_select5.bind('<KeyRelease>',list_update5)
        augment_select5.bind('<FocusIn>', show_dropdown5)

        augbox5 = tk.Listbox(self, selectmode=tk.SINGLE)
        augbox5.bind('<FocusIn>', hide_dropdown5)

        separator = ttk.Separator(self)
        separator.grid(row=5, column=0, pady=10, sticky='ew')

        button = ttk.Button(self, text='Calculate!', command=calculate_optimal)
        button.grid(row=6, column=0, padx=5, pady=(10,5), sticky='ew')

# Bonus Stats
class stat_adder(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent, text='Add Bonus Stats', padding=10)

        global ad_entry
        ad_entry = ttk.Entry(self,width=3)
        ad_entry.insert(0, 0)
        ad_entry.grid(row=0, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        ad_label = ttk.Label(self, text='AD')
        ad_label.grid(row=0, column=1, padx=10, sticky='ew')

        global ap_entry
        ap_entry = ttk.Entry(self,width=3)
        ap_entry.insert(0, 0)
        ap_entry.grid(row=1, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        ap_label = ttk.Label(self, text='AP')
        ap_label.grid(row=1, column=1, padx=10, sticky='ew')

        global as_entry
        as_entry = ttk.Entry(self,width=3)
        as_entry.insert(0, 0)
        as_entry.grid(row=2, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        as_label = ttk.Label(self, text='Attack Speed')
        as_label.grid(row=2, column=1, padx=10, sticky='ew')

        global crit_entry
        crit_entry = ttk.Entry(self,width=3)
        crit_entry.insert(0, 0)
        crit_entry.grid(row=3, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        crit_label = ttk.Label(self, text='Crit Chance')
        crit_label.grid(row=3, column=1, padx=10, sticky='ew')

        global hsp_entry
        hsp_entry = ttk.Entry(self,width=3)
        hsp_entry.insert(0, 0)
        hsp_entry.grid(row=4, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        hsp_label = ttk.Label(self, text='Heal Power')
        hsp_label.grid(row=4, column=1, padx=10, sticky='ew')

        global armor_entry
        armor_entry = ttk.Entry(self,width=3)
        armor_entry.insert(0, 0)
        armor_entry.grid(row=5, column=0, padx=(5,0), pady=(5, 10), sticky='ew')

        armor_label = ttk.Label(self, text='Armor')
        armor_label.grid(row=5, column=1, padx=10, sticky='ew')

        global mr_entry
        mr_entry = ttk.Entry(self,width=3)
        mr_entry.insert(0, 0)
        mr_entry.grid(row=6, column=0, padx=(5,0), pady=5, sticky='ew')

        mr_label = ttk.Label(self, text='Magic Resist')
        mr_label.grid(row=6, column=1, padx=10, sticky='nsew')

# Data Output
class itemoutput(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent, text='Item Output', padding=5)

        global build_label_var
        build_label_var = tk.StringVar()

        global hps_label_var
        hps_label_var = tk.StringVar()

        global stats_label_var
        stats_label_var = tk.StringVar()

        items_label = ttk.Label(self, textvariable=build_label_var)
        build_label_var.set('Calculate to see optimal build!')
        items_label.grid(row=0,column=0, sticky= 'w', padx=10, pady=(3,0))

        hps_label = ttk.Label(self, textvariable=hps_label_var)
        hps_label_var.set('Healing per second: ')
        hps_label.grid(row=1,column=0, sticky= 'w', padx=10, pady=(5,10))

# Gui Assembly
class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)

        options(self).grid(row=0, column=0, rowspan=3, padx=(0, 10), sticky='nsew')

        augment_box(self).grid(row=0, column=1, padx=10, rowspan=2, pady=(0,10), sticky='nsew')

        stat_adder(self).grid(row=0, column=2, rowspan=2, padx=(10,0), pady=(0,10), sticky='nsew')

        itemoutput(self).grid(row=2, column=1, columnspan=2, padx=(10,0), sticky='nsew')

sv_ttk.set_theme('dark')

App(root).pack(expand=True, fill='both')

root.mainloop()
