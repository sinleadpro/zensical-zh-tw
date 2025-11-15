# reCAPTCHA Configuration Guide

## Overview
!!! quote "What is reCAPTCHA?"
    reCAPTCHA is a bot verification service provided by Google, used to prevent malicious registrations and spam.


=== "Important Notes"
	- Requires prior Google reCAPTCHA registration
	- Only v3 is supported

=== "Applications"
	- Login/Registration page verification
	- Form spam protection

## Configuration
1. Go to [Google reCAPTCHA Console](https://www.google.com/recaptcha/admin)
2. Create a new key
3. Fill in the key in the backend settings field
## Next
- How to enable v2 and v3 simultaneously?
- How to test verification results?

## Integration
- Integrate with form API
- Integrate with marketing modules

## FAQ
??? question "Why isn't the CAPTCHA displaying?"
    Please ensure the domain name matches the Google key settings.

## See Also
- [Google Official reCAPTCHA Documentation](https://developers.google.com/recaptcha)
- [Other Security Settings](security.md)