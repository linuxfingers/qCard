def main():
    print('What are the contact details?')
    fname = input('First name: ')
    lname = input('Last name: ')
    email = input('E-mail: ' )
    company = input('Company: ')
    title = input('Title: ')
    phone = input('Phone number: ')
    address = input('Address: ')
    web = input('Website: ')
    okay()
    vcf_file = f'{fname.lower()}.vcf'
    print(f'Writing vCard to: {vcf_file}')
    okay()
    vcard = make_vcard(fname, lname, company, title, phone, address, email, web)
    write_vcard(vcf_file, vcard)

def make_vcard(
        fname,
        lname,
        company,
        title,
        phone,
        address,
        email,
        web):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        'VERSION:4.0',
        f'N:{lname};{fname}'
        f'FN:{fname} {lname}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
        ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])

def okay():
    okay = input('Is this okay? [yes/no] ')
    if okay in ['Yes', 'yes', 'YES', 'y', 'Y', 'ok']:
        return True
    else:
        print('Oh, cancelled.')
        exit(1)

if __name__ == "__main__":
    main()
