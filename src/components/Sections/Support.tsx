import { useState, FormEvent } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ReCAPTCHA from 'react-google-recaptcha';
import { useLanguage } from '../../hooks/useLanguage';
import { translations, Language } from '../../data/content';
import {
    Mail, Phone, MapPin, Send, User,
    AlertCircle, CheckCircle, Briefcase, HelpCircle,
    Calendar, Hash, Globe, ChevronDown
} from 'lucide-react';

type InquiryType = 'service' | 'support' | 'household';

interface FormData {
    // Common
    name: string;
    email: string;
    phone: string;
    company: string;
    inquiryType: InquiryType;

    // Service Request
    interestedService: string;
    budgetRange: string;
    startDate: string;
    location: string;

    // Support
    orderId: string;
    issueType: string;

    // Household
    householdOption: string;

    // Common Tail
    subject: string;
    message: string;
    consent: boolean;
}

const INITIAL_FORM: FormData = {
    name: '',
    email: '',
    phone: '',
    company: '',
    inquiryType: 'service',
    interestedService: '',
    budgetRange: '',
    startDate: '',
    location: '',
    orderId: '',
    issueType: '',
    householdOption: '',
    subject: '',
    message: '',
    consent: false
};

// Service option keys for translation mapping
const SERVICE_OPTION_KEYS = [
    'webDev', 'mobileDev', 'aiIntegration', 'consulting',
    'chatbot', 'software', 'machineLearning', 'solar', 'evCharger',
    'greenArch', 'hvacMep', 'automation', 'envServices',
    'security', 'accessControl', 'greenConst', 'smartHome', 'smartFarming',
    'other'
] as const;

// Household option keys
const HOUSEHOLD_OPTION_KEYS = ['plumbing', 'electrical', 'acRepair', 'cleaning', 'pestControl', 'gardening', 'other'] as const;

// Issue type keys for translation mapping
const ISSUE_TYPE_KEYS = ['technical', 'billing', 'accountAccess', 'featureRequest', 'other'] as const;

export default function Support() {
    const { t, language } = useLanguage();
    const form_t = translations.supportForm;

    // Helper function to get translated text
    const getText = (obj: Record<Language, string>) => obj[language] || obj['en'];

    // Form State
    const [form, setForm] = useState<FormData>(INITIAL_FORM);
    const [captchaToken, setCaptchaToken] = useState<string | null>(null);
    const [status, setStatus] = useState<'idle' | 'sending' | 'success' | 'error'>('idle');
    const [errorMessage, setErrorMessage] = useState('');

    // Config
    const SITE_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"; // Google Test Key

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setForm(prev => ({ ...prev, [name]: value }));
    };

    const handleTypeChange = (type: InquiryType) => {
        setForm(prev => ({
            ...prev,
            inquiryType: type,
            // Reset conditional fields when switching
            interestedService: '',
            budgetRange: '',
            startDate: '',
            location: '',
            orderId: '',
            issueType: '',
            householdOption: ''
        }));
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();


        // Strict Validation
        const requiredFields = ['name', 'email', 'phone', 'company', 'message'];
        if (form.inquiryType === 'service') {
            requiredFields.push('interestedService', 'startDate', 'location');
        } else if (form.inquiryType === 'support') {
            requiredFields.push('issueType', 'orderId');
        } else if (form.inquiryType === 'household') {
            requiredFields.push('householdOption');
        } else {
            requiredFields.push('subject');
        }

        const missingFields = requiredFields.filter(field => !form[field as keyof FormData]);

        if (missingFields.length > 0 || !form.consent) {
            setErrorMessage(getText(form_t.errors.requiredFields));
            setStatus('error');
            return;
        }

        if (!captchaToken) {
            setErrorMessage(getText(form_t.errors.captcha));
            setStatus('error');
            return;
        }

        // Destination Email for all inquiries
        const DESTINATION_EMAIL = "d95d5f9d747a3a0986f2e325dfe592a7";

        const destinationEmail = DESTINATION_EMAIL;

        setStatus('sending');
        setErrorMessage('');

        try {
            const response = await fetch(`https://formsubmit.co/ajax/${destinationEmail}`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    _subject: `New ${form.inquiryType.toUpperCase()} Inquiry from ${form.name}`,
                    _template: 'table', // FormSubmit's clean table layout
                    ...form
                })
            });

            if (response.ok) {
                setStatus('success');
                setForm(INITIAL_FORM);
                setCaptchaToken(null);
                setTimeout(() => setStatus('idle'), 5000);
            } else {
                setErrorMessage(getText(form_t.errors.general));
                setStatus('error');
            }
        } catch (error) {
            setErrorMessage(getText(form_t.errors.network));
            setStatus('error');
        }
    };

    // Get translated service options
    const getServiceOptions = () => {
        return SERVICE_OPTION_KEYS.map(key => ({
            key,
            label: getText(form_t.serviceOptions[key])
        }));
    };

    // Get translated household options
    const getHouseholdOptions = () => {
        return HOUSEHOLD_OPTION_KEYS.map(key => ({
            key,
            label: getText(form_t.householdOptions[key])
        }));
    };

    // Get translated issue types
    const getIssueTypes = () => {
        return ISSUE_TYPE_KEYS.map(key => ({
            key,
            label: getText(form_t.issueTypes[key])
        }));
    };

    // Get inquiry type label
    const getInquiryTypeLabel = (type: InquiryType) => {
        return getText(form_t.inquiryTypes[type]);
    };

    // Get message label based on inquiry type
    const getMessageLabel = () => {
        return getText(form_t.messageLabels[form.inquiryType]);
    };

    // Get message placeholder based on inquiry type
    const getMessagePlaceholder = () => {
        return getText(form_t.messagePlaceholders[form.inquiryType]);
    };

    // Get consent message based on inquiry type
    const getConsentMessage = () => {
        return getText(form_t.consentMessages[form.inquiryType]);
    };

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="pt-24 pb-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto min-h-screen"
        >
            <div className="text-center mb-16">
                <h2 className="text-4xl font-bold text-gray-900 mb-4">{t('nav.support')}</h2>
                <div className="w-24 h-1 bg-sky-500 mx-auto rounded-full"></div>
            </div>

            {/* Hero Image Section */}
            <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.2 }}
                className="max-w-4xl mx-auto mb-12"
            >
                <div className="relative h-64 md:h-80 rounded-2xl overflow-hidden shadow-2xl">
                    <img
                        src="./images/2.jpg"
                        alt="Support"
                        className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-sky-900/70 to-transparent flex items-end p-8">
                        <p className="text-white font-medium text-lg md:text-xl italic">
                            {getText(form_t.heroQuote)}
                        </p>
                    </div>
                </div>
            </motion.div>

            {/* Smart Form Section - Centered */}
            <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.3 }}
                className="max-w-3xl mx-auto"
            >
                <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100 relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-sky-100 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>

                    <div className="text-center mb-8">
                        <h3 className="text-3xl font-bold text-gray-800 mb-2 relative z-10">
                            {getText(form_t.formTitle)}
                        </h3>
                        <p className="text-gray-500">{getText(form_t.formSubtitle)}</p>
                    </div>

                    {/* Inquiry Type Selector - Tabs */}
                    <div className="grid grid-cols-3 gap-2 mb-8 p-1 bg-slate-100 rounded-xl z-10 relative">
                        {(['service', 'household', 'support'] as InquiryType[]).map((type) => (
                            <button
                                key={type}
                                type="button"
                                onClick={() => handleTypeChange(type)}
                                className={`py-2 px-1 rounded-lg text-sm font-semibold transition-all duration-300 capitalize flex items-center justify-center gap-2 ${form.inquiryType === type
                                    ? 'bg-white text-sky-600 shadow-md'
                                    : 'text-gray-500 hover:bg-white/50'
                                    }`}
                            >
                                {type === 'service' && <Briefcase size={16} />}
                                {type === 'support' && <HelpCircle size={16} />}
                                {type === 'household' && <User size={16} />}
                                <span className="hidden sm:inline">
                                    {getInquiryTypeLabel(type)}
                                </span>
                            </button>
                        ))}
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-5 relative z-10">
                        {status === 'error' && (
                            <div className="p-4 bg-red-50 text-red-600 rounded-xl flex items-center gap-2 text-sm font-medium animate-shake">
                                <AlertCircle size={18} />
                                {errorMessage}
                            </div>
                        )}

                        {/* Common: Contact Info */}
                        <div className="grid md:grid-cols-2 gap-5">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.fullName)} *</label>
                                <div className="relative">
                                    <User className="absolute left-3 top-3 text-gray-400" size={18} />
                                    <input
                                        type="text"
                                        name="name"
                                        value={form.name}
                                        onChange={handleInputChange}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder={getText(form_t.fullNamePlaceholder)}
                                    />
                                </div>
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.emailAddress)} *</label>
                                <div className="relative">
                                    <Mail className="absolute left-3 top-3 text-gray-400" size={18} />
                                    <input
                                        type="email"
                                        name="email"
                                        value={form.email}
                                        onChange={handleInputChange}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder={getText(form_t.emailPlaceholder)}
                                    />
                                </div>
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.phoneNumber)} *</label>
                                <div className="relative">
                                    <Phone className="absolute left-3 top-3 text-gray-400" size={18} />
                                    <input
                                        type="tel"
                                        name="phone"
                                        value={form.phone}
                                        onChange={handleInputChange}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder={getText(form_t.phonePlaceholder)}
                                    />
                                </div>
                            </div>
                            <div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.company)} *</label>
                                    <div className="relative">
                                        <Globe className="absolute left-3 top-3 text-gray-400" size={18} />
                                        <input
                                            type="text"
                                            name="company"
                                            value={form.company}
                                            onChange={handleInputChange}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                            placeholder={getText(form_t.companyPlaceholder)}
                                        />
                                    </div>
                                </div>
                            </div>

                            <AnimatePresence mode="wait">
                                {form.inquiryType === 'service' && (
                                    <motion.div
                                        key="service-fields"
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        exit={{ opacity: 0, height: 0 }}
                                        className="grid md:grid-cols-2 gap-5 overflow-hidden"
                                    >
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.serviceInterested)} *</label>
                                            <div className="relative">
                                                <Briefcase className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="interestedService"
                                                    value={form.interestedService}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">{getText(form_t.selectService)}</option>
                                                    {getServiceOptions().map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.startDate)} *</label>
                                            <div className="relative">
                                                <Calendar className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <input
                                                    type="date"
                                                    name="startDate"
                                                    value={form.startDate}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                                />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.locationLabel)} *</label>
                                            <div className="relative">
                                                <MapPin className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <input
                                                    type="text"
                                                    name="location"
                                                    value={form.location}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                                    placeholder={getText(form_t.locationValue)}
                                                />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}

                                {form.inquiryType === 'support' && (
                                    <motion.div
                                        key="support-fields"
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        exit={{ opacity: 0, height: 0 }}
                                        className="grid md:grid-cols-2 gap-5 overflow-hidden"
                                    >
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.issueType)} *</label>
                                            <div className="relative">
                                                <AlertCircle className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="issueType"
                                                    value={form.issueType}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">{getText(form_t.selectIssueType)}</option>
                                                    {getIssueTypes().map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.orderId)} *</label>
                                            <div className="relative">
                                                <Hash className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <input
                                                    type="text"
                                                    name="orderId"
                                                    value={form.orderId}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                                    placeholder={getText(form_t.orderIdPlaceholder)}
                                                />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}

                                {form.inquiryType === 'household' && (
                                    <motion.div
                                        key="household-fields"
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        exit={{ opacity: 0, height: 0 }}
                                        className="grid md:grid-cols-2 gap-5" // Added gap for consistency
                                    >
                                        <div className="md:col-span-2">
                                            <label className="block text-sm font-medium text-gray-700 mb-1">{getText(form_t.serviceInterested)} *</label>
                                            <div className="relative">
                                                <Briefcase className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="householdOption"
                                                    value={form.householdOption}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">{getText(form_t.selectService)}</option>
                                                    {getHouseholdOptions().map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}
                            </AnimatePresence>

                            {/* Message */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">
                                    {getMessageLabel()} *
                                </label>
                                <textarea
                                    name="message"
                                    rows={5}
                                    value={form.message}
                                    onChange={handleInputChange}
                                    className="w-full p-4 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all resize-none"
                                    placeholder={getMessagePlaceholder()}
                                />
                            </div>

                            {/* Consent Checkbox */}
                            <div className="flex items-start gap-3">
                                <div className="flex-shrink-0 mt-1">
                                    <input
                                        type="checkbox"
                                        id="consent"
                                        checked={form.consent}
                                        onChange={(e) => setForm(prev => ({ ...prev, consent: e.target.checked }))}
                                        className="w-5 h-5 text-sky-600 border-gray-300 rounded focus:ring-sky-500 cursor-pointer"
                                    />
                                </div>
                                <label htmlFor="consent" className="text-sm text-gray-600 cursor-pointer select-none">
                                    {getConsentMessage()}
                                </label>
                            </div>

                            {/* ReCAPTCHA */}
                            <div className="flex justify-center pt-2">
                                <ReCAPTCHA
                                    sitekey={SITE_KEY}
                                    onChange={(token) => setCaptchaToken(token)}
                                />
                            </div>

                            <div className="flex justify-center pt-2">
                                <button
                                    type="submit"
                                    disabled={status === 'sending' || status === 'success' || status === 'error'}
                                    className={`w-full py-4 rounded-xl font-bold text-white shadow-lg flex items-center justify-center gap-2 transition-all transform active:scale-95 ${status === 'success'
                                        ? 'bg-green-500 hover:bg-green-600'
                                        : 'bg-gradient-to-r from-sky-600 to-blue-800 hover:from-sky-500 hover:to-blue-700'
                                        }`}
                                >
                                    {status === 'sending' ? (
                                        <span className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                                    ) : status === 'success' ? (
                                        <>
                                            <CheckCircle size={20} />
                                            {getText(form_t.buttons.success)}
                                        </>
                                    ) : (
                                        <>
                                            <Send size={18} />
                                            {getText(form_t.buttons.submit)}
                                        </>
                                    )}
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </motion.div >
        </motion.div >
    );
}
