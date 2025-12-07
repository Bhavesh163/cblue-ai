import { useState, FormEvent } from 'react';
import { motion } from 'framer-motion';
import ReCAPTCHA from 'react-google-recaptcha';
import { useLanguage } from '../../hooks/useLanguage';
import { translations } from '../../data/content';
import { Mail, Phone, MapPin, Send, User, MessageSquare, AlertCircle, CheckCircle } from 'lucide-react';

export default function Support() {
    const { t, language } = useLanguage();
    const support = translations.support;

    // Form State
    const [form, setForm] = useState({ name: '', email: '', phone: '', subject: '', message: '' });
    const [captchaToken, setCaptchaToken] = useState<string | null>(null);
    const [status, setStatus] = useState<'idle' | 'sending' | 'success' | 'error'>('idle');
    const [errorMessage, setErrorMessage] = useState('');

    // Config
    const SITE_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"; // Google Test Key

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();

        // Strict Validation
        if (!form.name || !form.email || !form.phone || !form.subject || !form.message) {
            setErrorMessage("Please fill in all fields.");
            setStatus('error');
            return;
        }

        if (!captchaToken) {
            setErrorMessage("Please complete the reCAPTCHA verification.");
            setStatus('error');
            return;
        }

        setStatus('sending');
        setErrorMessage('');

        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1500));

        setStatus('success');
        setForm({ name: '', email: '', phone: '', subject: '', message: '' });
        setCaptchaToken(null);

        setTimeout(() => setStatus('idle'), 5000);
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

            <div className="grid md:grid-cols-2 gap-12 items-start">
                {/* Contact Info */}
                <motion.div
                    initial={{ x: -30, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: 0.2 }}
                    className="bg-white rounded-2xl shadow-xl overflow-hidden p-8 border border-gray-100"
                >
                    <h3 className="text-2xl font-bold text-gray-800 mb-8 border-b pb-4">
                        {support.title[language] || support.title['en']}
                    </h3>

                    <div className="space-y-6">
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
                                    Address
                                </p>
                                <p className="text-lg font-bold text-gray-900">
                                    Thailand
                                </p>
                            </div>
                        </div>
                    </div>
                </motion.div>

                {/* Image */}
                <motion.div
                    initial={{ x: 30, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: 0.4 }}
                    className="relative h-96 rounded-2xl overflow-hidden shadow-2xl"
                >
                    <img
                        src={support.image}
                        alt="Contact Us"
                        className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-sky-900/60 to-transparent flex items-end p-8">
                        <p className="text-white font-medium text-lg italic">
                            "We are here to help you build the future."
                        </p>
                    </div>
                </motion.div>
            </div>

            {/* Contact Form Section */}
            <motion.div
                initial={{ y: 30, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.6 }}
                className="mt-20 max-w-4xl mx-auto"
            >
                <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100 relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-sky-100 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>

                    <div className="text-center mb-10">
                        <h3 className="text-3xl font-bold text-gray-800 mb-2 relative z-10">
                            Send us a message
                        </h3>
                        <p className="text-gray-500">We'd love to hear from you. Fill out the form below.</p>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-6 relative z-10">
                        {status === 'error' && (
                            <div className="p-4 bg-red-50 text-red-600 rounded-xl flex items-center gap-2 text-sm font-medium animate-shake">
                                <AlertCircle size={18} />
                                {errorMessage}
                            </div>
                        )}

                        <div className="grid md:grid-cols-2 gap-6">
                            {/* Name */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">Name <span className="text-red-500">*</span></label>
                                <div className="relative">
                                    <span className="absolute left-3 top-3 text-gray-400">
                                        <User size={18} />
                                    </span>
                                    <input
                                        type="text"
                                        value={form.name}
                                        onChange={(e) => setForm({ ...form, name: e.target.value })}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder="Your Name"
                                    />
                                </div>
                            </div>

                            {/* Email */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">Email <span className="text-red-500">*</span></label>
                                <div className="relative">
                                    <span className="absolute left-3 top-3 text-gray-400">
                                        <Mail size={18} />
                                    </span>
                                    <input
                                        type="email"
                                        value={form.email}
                                        onChange={(e) => setForm({ ...form, email: e.target.value })}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder="your@email.com"
                                    />
                                </div>
                            </div>
                        </div>

                        <div className="grid md:grid-cols-2 gap-6">
                            {/* Phone */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">Phone Number <span className="text-red-500">*</span></label>
                                <div className="relative">
                                    <span className="absolute left-3 top-3 text-gray-400">
                                        <Phone size={18} />
                                    </span>
                                    <input
                                        type="tel"
                                        value={form.phone}
                                        onChange={(e) => setForm({ ...form, phone: e.target.value })}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder="081 234 5678"
                                    />
                                </div>
                            </div>

                            {/* Subject */}
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">Subject <span className="text-red-500">*</span></label>
                                <div className="relative">
                                    <span className="absolute left-3 top-3 text-gray-400">
                                        <AlertCircle size={18} />
                                    </span>
                                    <input
                                        type="text"
                                        value={form.subject}
                                        onChange={(e) => setForm({ ...form, subject: e.target.value })}
                                        className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all"
                                        placeholder="Inquiry Subject"
                                    />
                                </div>
                            </div>
                        </div>

                        {/* Message */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Message <span className="text-red-500">*</span></label>
                            <div className="relative">
                                <span className="absolute left-3 top-3 text-gray-400">
                                    <MessageSquare size={18} />
                                </span>
                                <textarea
                                    rows={5}
                                    value={form.message}
                                    onChange={(e) => setForm({ ...form, message: e.target.value })}
                                    className="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-100 transition-all resize-none"
                                    placeholder="How can we help you?"
                                />
                            </div>
                        </div>

                        {/* ReCAPTCHA */}
                        <div className="flex justify-center">
                            <ReCAPTCHA
                                sitekey={SITE_KEY}
                                onChange={(token) => setCaptchaToken(token)}
                            />
                        </div>

                        <div className="flex justify-center pt-2">
                            <button
                                type="submit"
                                disabled={status === 'sending' || status === 'success' || status === 'error'}
                                className={`w-full md:w-1/3 py-3.5 rounded-xl font-bold text-white shadow-lg flex items-center justify-center gap-2 transition-all transform active:scale-95 ${status === 'success'
                                    ? 'bg-green-500 hover:bg-green-600'
                                    : 'bg-gradient-to-r from-sky-600 to-blue-800 hover:from-sky-500 hover:to-blue-700'
                                    }`}
                            >
                                {status === 'sending' ? (
                                    <span className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                                ) : status === 'success' ? (
                                    <>
                                        <CheckCircle size={20} />
                                        Message Sent!
                                    </>
                                ) : (
                                    <>
                                        <Send size={18} />
                                        Send Message
                                    </>
                                )}
                            </button>
                        </div>
                    </form>
                </div>
            </motion.div>
        </motion.div>
    );
}
