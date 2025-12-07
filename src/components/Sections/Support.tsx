import { useState, FormEvent } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ReCAPTCHA from 'react-google-recaptcha';
import { useLanguage } from '../../hooks/useLanguage';
import { translations } from '../../data/content';
import {
    Mail, Phone, MapPin, Send, User, MessageSquare,
    AlertCircle, CheckCircle, Briefcase, HelpCircle,
    DollarSign, Calendar, Hash, Globe, ChevronDown
} from 'lucide-react';

type InquiryType = 'service' | 'support' | 'general';

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

    // Support
    orderId: string;
    issueType: string;

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
    inquiryType: 'general',
    interestedService: '',
    budgetRange: '',
    startDate: '',
    orderId: '',
    issueType: '',
    subject: '',
    message: '',
    consent: false
};

const SERVICE_OPTIONS = [
    "Web Development",
    "Mobile App Development",
    "AI Integration",
    "Consulting",
    "Other"
];

const BUDGET_OPTIONS = [
    "Less than $5,000",
    "$5,000 - $10,000",
    "$10,000 - $25,000",
    "$25,000 - $50,000",
    "$50,000+"
];

const ISSUE_TYPES = [
    "Technical Issue",
    "Billing / Payment",
    "Account Access",
    "Feature Request",
    "Other"
];

export default function Support() {
    const { t, language } = useLanguage();
    const support = translations.support;

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
            orderId: '',
            issueType: ''
        }));
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();

        // Strict Validation
        const requiredFields = ['name', 'email', 'phone', 'message'];
        if (form.inquiryType === 'service') {
            requiredFields.push('interestedService', 'budgetRange', 'startDate');
        } else if (form.inquiryType === 'support') {
            requiredFields.push('issueType');
        } else {
            requiredFields.push('subject');
        }

        const missingFields = requiredFields.filter(field => !form[field as keyof FormData]);

        if (missingFields.length > 0 || !form.consent) {
            setErrorMessage("Please fill in all required fields and accept the terms.");
            setStatus('error');
            return;
        }

        if (!captchaToken) {
            setErrorMessage("Please complete the reCAPTCHA verification.");
            setStatus('error');
            return;
        }

        // Determine Destination Email based on Inquiry Type
        // TO USER: Replace these with your actual email addresses
        const GMAIL_ADDRESS = "your-gmail-placeholder@gmail.com";
        const HOTMAIL_ADDRESS = "your-hotmail-placeholder@hotmail.com";

        const destinationEmail = form.inquiryType === 'support'
            ? HOTMAIL_ADDRESS
            : GMAIL_ADDRESS;

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
                setErrorMessage("Something went wrong. Please try again later.");
                setStatus('error');
            }
        } catch (error) {
            setErrorMessage("Network error. Please check your connection.");
            setStatus('error');
        }
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

            <div className="grid lg:grid-cols-2 gap-12 items-start">
                {/* Visual / Contact Info Side */}
                <div className="space-y-8">
                    {/* Image */}
                    <motion.div
                        initial={{ x: -30, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        transition={{ delay: 0.2 }}
                        className="relative h-64 md:h-80 rounded-2xl overflow-hidden shadow-2xl"
                    >
                        <img
                            src={support.image}
                            alt="Contact support"
                            className="w-full h-full object-cover"
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-sky-900/80 to-transparent flex items-end p-8">
                            <p className="text-white font-medium text-lg italic">
                                "We are here to help you build the future."
                            </p>
                        </div>
                    </motion.div>

                    {/* Contact Cards */}
                    <motion.div
                        initial={{ x: -30, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        transition={{ delay: 0.4 }}
                        className="bg-white rounded-2xl shadow-xl overflow-hidden p-8 border border-gray-100"
                    >
                        <h3 className="text-2xl font-bold text-gray-800 mb-6 border-b pb-4">
                            Contact Details
                        </h3>
                        <div className="space-y-4">
                            {support.items.map((item, index) => (
                                <div key={index} className="flex items-center space-x-4 p-4 bg-slate-50 rounded-xl hover:bg-sky-50 transition-colors duration-300">
                                    <div className="bg-white p-3 rounded-full shadow-sm text-sky-600">
                                        {item.label['en'] === 'Email' ? <Mail /> : <Phone />}
                                    </div>
                                    <div>
                                        <p className="text-sm text-gray-500 font-medium uppercase tracking-wider">
                                            {item.label[language] || item.label['en']}
                                        </p>
                                        <p className="text-lg font-bold text-gray-900">
                                            {item.value}
                                        </p>
                                    </div>
                                </div>
                            ))}
                            <div className="flex items-center space-x-4 p-4 bg-slate-50 rounded-xl hover:bg-sky-50 transition-colors duration-300">
                                <div className="bg-white p-3 rounded-full shadow-sm text-sky-600">
                                    <MapPin />
                                </div>
                                <div>
                                    <p className="text-sm text-gray-500 font-medium uppercase tracking-wider">
                                        Location
                                    </p>
                                    <p className="text-lg font-bold text-gray-900">
                                        Bangkok, Thailand
                                    </p>
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </div>

                {/* Smart Form Section */}
                <motion.div
                    initial={{ x: 30, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: 0.6 }}
                >
                    <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100 relative overflow-hidden">
                        <div className="absolute top-0 right-0 w-32 h-32 bg-sky-100 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>

                        <div className="text-center mb-8">
                            <h3 className="text-3xl font-bold text-gray-800 mb-2 relative z-10">
                                How can we help?
                            </h3>
                            <p className="text-gray-500">Select an option below to get started.</p>
                        </div>

                        {/* Inquiry Type Selector - Tabs */}
                        <div className="grid grid-cols-3 gap-2 mb-8 p-1 bg-slate-100 rounded-xl z-10 relative">
                            {(['service', 'support', 'general'] as InquiryType[]).map((type) => (
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
                                    {type === 'general' && <MessageSquare size={16} />}
                                    <span className="hidden sm:inline">
                                        {type === 'service' ? 'Start Project' : type === 'support' ? 'Get Support' : 'General'}
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
                                    <label className="block text-sm font-medium text-gray-700 mb-1">Full Name *</label>
                                    <div className="relative">
                                        <User className="absolute left-3 top-3 text-gray-400" size={18} />
                                        <input
                                            type="text"
                                            name="name"
                                            value={form.name}
                                            onChange={handleInputChange}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                            placeholder="John Doe"
                                        />
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">Email Address *</label>
                                    <div className="relative">
                                        <Mail className="absolute left-3 top-3 text-gray-400" size={18} />
                                        <input
                                            type="email"
                                            name="email"
                                            value={form.email}
                                            onChange={handleInputChange}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                            placeholder="john@example.com"
                                        />
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">Phone Number *</label>
                                    <div className="relative">
                                        <Phone className="absolute left-3 top-3 text-gray-400" size={18} />
                                        <input
                                            type="tel"
                                            name="phone"
                                            value={form.phone}
                                            onChange={handleInputChange}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                            placeholder="+1 (555) 000-0000"
                                        />
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">Company (Optional)</label>
                                    <div className="relative">
                                        <Globe className="absolute left-3 top-3 text-gray-400" size={18} />
                                        <input
                                            type="text"
                                            name="company"
                                            value={form.company}
                                            onChange={handleInputChange}
                                            className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                            placeholder="Acme Inc."
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
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Service Interested In *</label>
                                            <div className="relative">
                                                <Briefcase className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="interestedService"
                                                    value={form.interestedService}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">Select a service</option>
                                                    {SERVICE_OPTIONS.map(opt => <option key={opt} value={opt}>{opt}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Budget Range *</label>
                                            <div className="relative">
                                                <DollarSign className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="budgetRange"
                                                    value={form.budgetRange}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">Select budget</option>
                                                    {BUDGET_OPTIONS.map(opt => <option key={opt} value={opt}>{opt}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                        <div className="md:col-span-2">
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Preferred Start Date *</label>
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
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Type of Issue *</label>
                                            <div className="relative">
                                                <AlertCircle className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <select
                                                    name="issueType"
                                                    value={form.issueType}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all appearance-none bg-white"
                                                >
                                                    <option value="">Select issue type</option>
                                                    {ISSUE_TYPES.map(opt => <option key={opt} value={opt}>{opt}</option>)}
                                                </select>
                                                <ChevronDown className="absolute right-3 top-3 text-gray-400 pointer-events-none" size={18} />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Order ID (Optional)</label>
                                            <div className="relative">
                                                <Hash className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <input
                                                    type="text"
                                                    name="orderId"
                                                    value={form.orderId}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                                    placeholder="#12345"
                                                />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}

                                {form.inquiryType === 'general' && (
                                    <motion.div
                                        key="general-fields"
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: 'auto' }}
                                        exit={{ opacity: 0, height: 0 }}
                                    >
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Subject *</label>
                                            <div className="relative">
                                                <MessageSquare className="absolute left-3 top-3 text-gray-400" size={18} />
                                                <input
                                                    type="text"
                                                    name="subject"
                                                    value={form.subject}
                                                    onChange={handleInputChange}
                                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                                    placeholder="Inquiry Subject"
                                                />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}
                            </AnimatePresence>

                            {/* Message */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">
                                    {form.inquiryType === 'service' ? 'Project Details / Requirements *'
                                        : form.inquiryType === 'support' ? 'Description of Problem *'
                                            : 'Message *'}
                                </label>
                                <textarea
                                    name="message"
                                    rows={5}
                                    value={form.message}
                                    onChange={handleInputChange}
                                    className="w-full p-4 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all resize-none"
                                    placeholder={form.inquiryType === 'service' ? 'Tell us about your project goals...' : 'Please describe the issue you are facing...'}
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
                                    {form.inquiryType === 'service'
                                        ? "I confirm the information provided is accurate and agree to allow the team to contact me regarding my project."
                                        : form.inquiryType === 'support'
                                            ? "I authorize your team to review my request and contact me with updates."
                                            : "I agree to the privacy policy and authorize you to contact me."}
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
                                            Request Sent!
                                        </>
                                    ) : (
                                        <>
                                            <Send size={18} />
                                            Submit Request
                                        </>
                                    )}
                                </button>
                            </div>
                        </form>
                    </div>
                </motion.div>
            </div>
        </motion.div>
    );
}

