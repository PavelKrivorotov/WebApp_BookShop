import * as yup from 'yup';
import { checkBookIsbn } from '../http/request';

export const IsbnValidation = yup
    .string()
    .test({
        name: 'isbn-test',
        skipAbsent: true,
        async test(value, ctx) {
            if (!(/^[0-9]{6}$/.test(value))) {
                return ctx.createError({message: 'isbn can containt only 6 characters of numbers (0-9)!'})
            }

            try {
                await checkBookIsbn(Number(value))
                return ctx.createError({message: 'This book ISBN already exists!'})
            }
            catch (error) {
                return true;
            }
        }
    })
    .required();


export const TitleValidation = yup
    .string()
    .max(150)
    .required();

export const PageValidation = yup
    .string()
    .matches(
        /^[1-9]{1}[0-9]{0,3}$/,
        'page can only characters of numbers (0-9) and less than 9999!'
    )
    .required();

export const StateValidation = yup
    .string()
    .required();

export const AuthorOrCategoryValidation = yup
    .array()
    .min(1);

export const ImageValidation = yup
    .mixed()
    .test({
        name:'test-1',
        skipAbsent: true,
        test(value, ctx) {
            if (value == "") {
                return ctx.createError({message:'image is required field!'})
            }
            if (value[0].size > 1*1024*1024) {
                return ctx.createError({message: 'image size more than 1Mb!'});
            }
            return true;
        },
        message: 'image size can`t be more then 1Mb!'
        })
    .required();
