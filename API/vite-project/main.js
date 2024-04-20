import { GoogleGenerativeAI } from "@google/generative-ai";

const API_KEY = 'YOUR API KEY'

const genAI = new GoogleGenerativeAI(process.env.API_KEY);

const model = genAI.getGenerativeModel({ model: "MODEL_NAME"});
